# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def iterateTree(node):
            if node.val in (0,1):
                return node.val
            elif node.val == 2:
                return iterateTree(node.left) or iterateTree(node.right)
            else:
                return iterateTree(node.left) or iterateTree(node.right)
        return iterateTree(root)