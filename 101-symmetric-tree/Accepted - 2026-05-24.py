# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def left2text(node):
            if not node:
                return "#"
            out = str(node.val)
            out += left2text(node.left)
            out += left2text(node.right)
            return out
        
        def right2text(node):
            if not node:
                return "#"
            out = str(node.val)
            out += left2text(node.right)
            out += left2text(node.left)
            return out
        
        return right2text(root.right) == left2text(root.left)