# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev, node = node, node.next
        while node:
            while node and node.val == prev.val:
                node = node.next
            prev.next = node
            if node:
                prev, node = node, node.next
        return head
    