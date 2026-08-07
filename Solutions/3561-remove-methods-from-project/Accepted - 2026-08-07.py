from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = {x: [] for x in range(n)}

        for a, b in invocations:
            graph[a].append(b)

        out = []

        q = [k]
        seen = set()

        while q:
            node = q.pop()
            seen.add(node)

            for v in graph[node]:
                if v not in seen:
                    q.append(v)
                seen.add(v)
        
        for a, b in invocations:
            if a not in seen and b in seen:
                return list(range(n))

        for i in range(n):
            if i not in seen:
                out.append(i)
        return out