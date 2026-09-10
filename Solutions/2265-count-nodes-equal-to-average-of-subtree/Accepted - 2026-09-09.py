# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        out = 0
        def DFS(node):
            nonlocal out
            if not node:
                return 0, 0
            left = DFS(node.left)
            right = DFS(node.right)
            totalSum = (left[0] + right[0] + node.val)
            subtree = totalSum // (left[1] + right[1] + 1)
            if subtree == node.val:
                out += 1
            return totalSum, left[1] + right[1] + 1 
        
        DFS(root)
        return out