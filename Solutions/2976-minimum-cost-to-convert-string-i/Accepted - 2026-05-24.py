class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = float("inf")
        graph = [[INF for _ in range(26)] for _ in range(26)]
        n = len(original)
        for i in range(n):
            u = ord(original[i]) - ord('a')
            v = ord(changed[i]) - ord('a')
            graph[u][v] = min(graph[u][v], cost[i])
            graph[u][u] = 0
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if graph[i][k] + graph[k][j] < graph[i][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]
        
        out = 0
        for s, t in zip(source, target):
            u, v = ord(s) - ord('a'), ord(t) - ord('a')
            if graph[u][v] == INF:
                return - 1
            out += graph[u][v]
        return out
