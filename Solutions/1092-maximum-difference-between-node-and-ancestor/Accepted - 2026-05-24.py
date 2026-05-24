# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal max_dif
            if not root:
                return float("inf"), float("-inf")
            min_left, max_left = dfs(root.left)
            min_right, max_right = dfs(root.right)

            actual_min = min(min_left, min_right, root.val)
            actual_max = max(max_left, max_right, root.val)
        
            if abs(actual_min - root.val) > max_dif:
                max_dif = abs(actual_min - root.val)
            if abs(actual_max - root.val) > max_dif:
                max_dif = abs(actual_max - root.val)
            return actual_min, actual_max
        max_dif = 0
        dfs(root)
        return max_dif
