# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def flip(node1, node2):
            if node1 == None and node2 == None:
                return True
            if (node1 == None and node2 != None) or (node2 == None and node1 != None) or (node1.val != node2.val):
                return False
            if flip(node1.right, node2.left) and (node1.left, node1.right):
                return True
            return False
        return flip(root1, root2)