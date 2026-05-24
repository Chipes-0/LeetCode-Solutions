# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        stack = [root]
        path = []

        while stack:
            root = stack[-1]
            if path and path[-1] == root:
                result.append(root.val)
                stack.pop()
                path.pop()
            else:
                path.append(root)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return result