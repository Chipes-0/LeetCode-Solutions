# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        N = 0
        node = head
        while node:
            N += 1
            node = node.next
        nodes_per_list = N // k
        remaining = N % k
        out = []
        for _ in range(k):
            i = 0
            if head:
                out.append(head)
            else:
                out.append(None)
            while i < (nodes_per_list + (remaining & 1)) - 1:
                head = head.next
                i += 1
            remaining -= 1
            if head:
                temp = head.next
                head.next = None
                head = temp
        return out