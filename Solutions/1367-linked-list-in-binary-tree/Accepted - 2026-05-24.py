# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(node, l):
            if not l:
                return True
            if not node:
                return False
            if node.val != l.val:
                return False
            return dfs(node.left, l.next) or dfs(node.right, l.next)

        def is_path(node, head):
            if not node:
                return False
            if dfs(node, head):
                return True
            return is_path(node.left, head) or is_path(node.right, head)

        return is_path(root, head)