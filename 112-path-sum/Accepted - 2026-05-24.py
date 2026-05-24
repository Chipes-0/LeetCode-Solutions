# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr):
            if not node:
                return curr == targetSum
            l = dfs(node.left, curr + node.val)
            r = dfs(node.right, curr + node.val)
            
            return l or r
        if not root:
            return False
        return dfs(root, 0)
