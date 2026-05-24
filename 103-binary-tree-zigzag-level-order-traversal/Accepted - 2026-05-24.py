# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        stack = [(root, 0)]
        while stack:
            node, deep = stack.pop(0)
            if not node:
                continue
            print(node.val, deep)
            if deep == len(out):
                out.append([])
            out[deep].append(node.val)
            if deep % 2 == 0:
                stack.append((node.right, deep+1))
                stack.append((node.left, deep+1))
            else:
                stack.append((node.left, deep+1))
                stack.append((node.right, deep+1))
                
        return out

            