# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        print(p.val, q.val)
        if p.val != q.val:
            return False
        if (p.left and not q.left) or (not p.left and q.left):
            return False
        if (p.right and not q.right) or (not p.right and q.right):
            return False
        if p.left:
            if not self.isSameTree(p.left, q.left):
                return False
        if p.right:
            if not self.isSameTree(p.right, q.right):
                return False
        return True