from collections import defaultdict
from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(num, parent, depth):
            max_depth = depth
            for node in graph[num]:
                if node != parent:
                    max_depth = max(max_depth, dfs(node, num, depth + 1))
            return max_depth
        
        max_depth = dfs(1, 0, 0)
        out = pow(2, max_depth - 1, 10**9 + 7)
        return out