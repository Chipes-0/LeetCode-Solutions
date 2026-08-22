# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        m = {}
        children = []
        for desc in descriptions:
            if desc[0] not in m:
                m[desc[0]] = TreeNode(desc[0])
            if desc[1] not in m:
                m[desc[1]] = TreeNode(desc[1])
            if desc[2]:
                m[desc[0]].left = m[desc[1]]
            else:
                m[desc[0]].right = m[desc[1]]
            children.append(desc[1])
        for val in m.keys():
            if val not in children:
                return m[val]