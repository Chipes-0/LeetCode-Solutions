from typing import List
from collections import defaultdict
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = defaultdict(list)
        for edge in edges:
            u, v, w = edge
            graph[u].append((v, w))
        
        def dijkstra(src):
            dist = [[float("inf") for _ in range(k + 1)] for _ in range(n)]
            dist[0][1] = 0

            pq = []
            heapq.heappush(pq, (0, src, 1))
            
            while pq:
                d, u, count = heapq.heappop(pq)
                if d > dist[u][count]:
                    continue
                
                for x in graph[u]:
                    v = x[0]
                    weight = x[1]
                    new_count = 1 if labels[u] != labels[v] else count + 1

                    if new_count <= k:
                        if dist[v][new_count] > d + weight:
                            dist[v][new_count] = d + weight
                            heapq.heappush(pq, (dist[v][new_count], v, new_count))
            return dist
        
        distances = dijkstra(0)
        out = float("inf")
        for n in distances[n - 1]:
            out = min(out, n)

        if out != float("inf"):
            return out
        return -1