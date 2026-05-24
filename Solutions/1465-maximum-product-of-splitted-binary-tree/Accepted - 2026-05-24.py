# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        modulo = 10 ** 9 + 7

        def rec_sum(node):
            if not node:
                return 0
            return (node.val + rec_sum(node.left) + rec_sum(node.right)) % modulo

        total = root.val + rec_sum(root.left) + rec_sum(root.right)
        total %= modulo


        out = float("-inf")
        def rec_max(node):
            nonlocal out
            nonlocal total
            if not node:
                return 0
            subtree = node.val + rec_max(node.left) + rec_max(node.right)
            out = max((total - subtree) * subtree, out) % modulo
            return subtree
        
        rec_max(root.left)
        rec_max(root.right)
        return out