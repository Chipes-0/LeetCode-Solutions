from typing import List

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        path = []

        while stack:
            node = stack[-1]
            if path and path[-1] == node:
                res.append(node.val)
                stack.pop()
                path.pop()
            else:
                path.append(node)
                for element in reversed(node.children):
                    stack.append(element)
        return res