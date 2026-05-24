# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min = None
        def treeInOrder(node):
            nonlocal p, min_dif
            if node is None:
                return
            treeInOrder(node.left)
            if p != None:
                min_dif = abs(p - node.val) if abs(p - node.val) < min_dif else min_dif
            p = node.val
            treeInOrder(node.right)

        min_dif = float('inf')
        p = None
        treeInOrder(root)
        return min_dif