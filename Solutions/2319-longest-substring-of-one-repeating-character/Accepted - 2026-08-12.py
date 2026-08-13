from typing import List

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        class Node:
            def __init__(self, lch, rch, prefix = 1, suffix = 1, best = 1, length = 1):
                self.left_char = lch
                self.right_char = rch
                self.prefix = prefix
                self.suffix = suffix
                self.best = best
                self.length = length

            def __repr__(self):
                return (
                    f"Node("
                    f"left={self.left_char}, "
                    f"right={self.right_char}, "
                    f"prefix={self.prefix}, "
                    f"suffix={self.suffix}, "
                    f"best={self.best}, "
                    f"length={self.length})"
                )
            
        
        def merge(a, b):
            val = 0
            if a.right_char == b.left_char:
                val = a.suffix + b.prefix
            best = max(a.best, val, b.best)

            if a.prefix == a.length and a.right_char == b.left_char:
                prefix = a.length + b.prefix
            else:
                prefix = a.prefix

            if b.suffix == b.length and a.right_char == b.left_char:
                suffix = b.length + a.suffix
            else:
                suffix = b.suffix
            length = a.length + b.length
            return Node(a.left_char, b.right_char, prefix, suffix, best, length)
                
        class SegTree:
            def __init__(self, arr):
                n = len(arr)
                size = 1
                while size < n:
                    size *= 2
                self.n = size
                self.tree = [None] * (2 * size)

                for i in range(n):
                    self.tree[size + i] = Node(arr[i], arr[i])

                for i in range(size - 1, 0, -1):
                    a = self.tree[2 * i]
                    b = self.tree[2 * i + 1]

                    if a is None:
                        self.tree[i] = b
                    elif b is None:
                        self.tree[i] = a
                    else:
                        self.tree[i] = merge(a, b)           
                
            def update(self, index, value):
                pos = self.n + index
                self.tree[pos] = Node(value, value)
                while pos > 1:
                    pos //= 2
                    a = self.tree[2 * pos]
                    b = self.tree[2 * pos + 1]

                    if a is None:
                        self.tree[pos] = b
                    elif b is None:
                        self.tree[pos] = a
                    else:
                        self.tree[pos] = merge(a, b)
            
        
        segTree = SegTree(s)
        out = []
        for i in range(len(queryCharacters)):
            index = queryIndices[i]
            ch = queryCharacters[i]
            segTree.update(index, ch)
            out.append(segTree.tree[1].best)
        return out