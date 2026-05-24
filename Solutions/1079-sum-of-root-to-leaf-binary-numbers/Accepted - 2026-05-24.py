# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        out = 0
        curr = []
        def dfs(node):
            nonlocal out
            if not node:
                out += int("".join(curr), 2)
                return
            else:
                curr.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            curr.pop(-1)
        dfs(root)
        return out // 2