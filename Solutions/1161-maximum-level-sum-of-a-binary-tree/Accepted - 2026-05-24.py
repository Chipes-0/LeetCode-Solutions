# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
import operator

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def iterateTree(node, lvl):
            nonlocal levels
            if node == None:
                return
            iterateTree(node.left, lvl + 1)
            levels[lvl] += node.val
            iterateTree(node.right, lvl + 1)
        levels = defaultdict(int)
        iterateTree(root, 1)
        
        return max(levels.items(), key = operator.itemgetter(1))[0]
