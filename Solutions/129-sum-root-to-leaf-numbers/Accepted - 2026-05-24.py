# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def iterateTree(node, value):
            out = 0
            
            if not node.left and not node.right:
                return value
            
            if node.left:
                out += iterateTree(node.left, value)
            if node.right:
                out += iterateTree(node.right, value)
            return out
        
        return iterateTree(root, 0)