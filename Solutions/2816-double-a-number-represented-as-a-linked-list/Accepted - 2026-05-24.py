# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        out = None
        def reverse(node):
            nonlocal out
            if not node.next:
                node.val = node.val * 2
                carry = (node.val) // 10
                node.val = node.val % 10
                out = node
                return carry, out
            carry, out = reverse(node.next)
            node.val = (node.val * 2) + carry
            carry = (node.val) // 10
            node.val = node.val % 10
            node.next = out
            out = node
            return carry, out
        carry, out = reverse(head)
        if carry:
            out = ListNode(carry, out)
        return out
            