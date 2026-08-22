from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        df = defaultdict(list)
        for u, v in edges:
            df[u].append(v)
        visited = []
        queue = [source]
        while queue:
            q = queue.pop(0)
            visited.append(q)
            if q == destination:
                return True
            for n in df[q]:
                if n not in visited:
                    queue.append(n)
        return False