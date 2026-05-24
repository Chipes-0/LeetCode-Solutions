# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(level, left, right):
            if not left or not right:
                return 
            if not (level & 1):
                left.val, right.val = right.val, left.val

            dfs(level + 1, left.left, right.right)
            dfs(level + 1, left.right, right.left)

        dfs(0, root.left, root.right)
        return root