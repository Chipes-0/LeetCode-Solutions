# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def iterateTree(node):
            if not node.left and not node.right:
                return chr(ord('a') + node.val)
            min_l = None
            min_r = None
            if node.left:
                min_l = iterateTree(node.left)
            if node.right:
                min_r = iterateTree(node.right)
            if not min_l:
                return min_r + chr(ord('a') + node.val)
            if not min_r:
                return min_l + chr(ord('a') + node.val)
            return min(min_l, min_r) + chr(ord('a') + node.val)
        return iterateTree(root)