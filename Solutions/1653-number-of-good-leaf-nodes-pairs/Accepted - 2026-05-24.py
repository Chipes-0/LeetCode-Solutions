# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        out = 0
        paths = []
        def iterateTree(node, path):
            if not node.left and not node.right:
                paths.append(path)
            path.append(node.val)
            if node.left:
                iterateTree(node.left, path[:])
            
            if node.right:
                iterateTree(node.right, path[:])
            
        iterateTree(root, [])
        print(paths)
        for i in range(len(paths)):
            for j in range(i + 1, len(paths)):
                index = 0
                while(paths[i][index] == paths[j][index]):
                    index += 1
                if len(paths[i]) + len(paths[j]) - (index * 2) <= distance:
                    out += 1
        return out
