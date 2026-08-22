# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        layer = root.val
        level = -1
        nodes = [root]
        while nodes:
            node = nodes.pop(0)
            if node.val == layer:
                if node.left:
                    layer = node.left.val
                level += 1
            if level % 2 == 0 and node.val % 2 == 0:
                return False
            elif level % 2 == 1 and node.val % 2 == 1:
                return False
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return True