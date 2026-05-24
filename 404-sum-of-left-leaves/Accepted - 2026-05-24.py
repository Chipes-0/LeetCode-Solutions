# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        out = 0
        def iterateTree(node, side):
            nonlocal out
            if not node.left and not node.right:
                if side == "l":
                    out += node.val
                return
            if node.left:
                iterateTree(node.left, "l")
            if node.right:
                iterateTree(node.right, "r")
            
        iterateTree(root, "n")
        return out
