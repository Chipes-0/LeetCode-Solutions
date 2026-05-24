# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        frecuency = defaultdict(int)
        def iterateTree(node, counter, prev):
            if not node:
                parity = 0
                for val in counter.values():
                    parity += val % 2
                    if parity == 2:
                        counter[prev] -= 1
                        return 0
                counter[prev] -= 1
                return 1
            counter[node.val] += 1
            return iterateTree(node.right, counter, node.val) + iterateTree(node.left, counter, node.val)
        return iterateTree(root, frecuency, None) - 1
