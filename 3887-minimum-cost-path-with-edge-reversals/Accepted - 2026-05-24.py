class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        edges_d = {}
        for e in edges:
            if e[1] not in edges_d:
                edges_d[e[1]] = []
            edges_d[e[1]].append((e[0], e[2] * 2))
        
            if e[0] not in edges_d:
                edges_d[e[0]] = []
            edges_d[e[0]].append((e[1], e[2]))
        
        def djs(edgs, src):
            V = n
            pq = []
            dist = [float("inf")] * n
            
            dist[src] = 0
            heapq.heappush(pq, (0, src))

            while pq:
                d, u = heapq.heappop(pq)

                if d > dist[u]:
                    continue
                for v, w in edgs[u]:

                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        heapq.heappush(pq, (dist[v], v))
            return dist[n - 1]
        
        return djs(edges_d, 0)