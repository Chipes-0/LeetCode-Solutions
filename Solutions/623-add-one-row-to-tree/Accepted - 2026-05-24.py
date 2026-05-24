# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def iterateTree(node, d):
            if not node:
                return
            if d == depth - 1:
                if node.left:
                    node.left = TreeNode(1, node.left, None)
                else:
                    node.left = TreeNode(1)
                if node.right:
                    node.right = TreeNode(1, None, node.right)
                else:
                    node.right = TreeNode(1)
                return 
            iterateTree(node.left, d + 1)
            iterateTree(node.right, d + 1)
            return 
        iterateTree(root, 1)
        return root