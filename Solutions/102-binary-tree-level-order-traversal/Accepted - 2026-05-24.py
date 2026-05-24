# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        queue = [(root, 0)]
        l = 0
        arr = []
        while queue:
            node, level = queue.pop(0)
            if not node:
                continue
            if level != l:
                out.append(arr)
                arr = []
                l += 1
            arr.append(node.val)
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
        if arr:
            out.append(arr)
        return out
            