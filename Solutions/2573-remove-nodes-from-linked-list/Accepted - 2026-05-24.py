# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        out = None
        def reverse(node):
            nonlocal out
            if not node.next:
                out = node
                return
            reverse(node.next)
            if out.val <= node.val:
                node.next = out
                out = node
        reverse(head)
        return out
            