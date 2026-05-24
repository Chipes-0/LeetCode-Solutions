# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = [] # max 500
        if not head:
            return None
        node = head 
        while node:
            nodes.append(node)
            node = node.next 
        N = len(nodes)

        rotate = k % N
        last = N - rotate
        nodes[last - 1].next = None
        nodes[-1].next = nodes[0]
        head = nodes[last]
        return head