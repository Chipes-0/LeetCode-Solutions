class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        class DSU:
            def __init__(self, n):
                self.rank = [0] * n
                self.parent = [0] * n

                for i in range(n):
                    self.parent[i] = i
            
            def find(self, num):
                if self.parent[num] != num:
                    self.parent[num] = self.find(self.parent[num])
                return self.parent[num]

            def union(self, a, b):
                ra, rb = self.find(a), self.find(b)
                if ra == rb:
                    return
                if self.rank[ra] < self.rank[rb]:
                    self.parent[ra] = rb
                elif self.rank[ra] > self.rank[rb]:
                    self.parent[rb] = ra
                else:
                    self.parent[rb] = ra
                    self.rank[ra] += 1
        N = len(edges)
        dsu = DSU(N + 1)
        for i in range(N):
            a, b = edges[i]
            if dsu.find(a) == dsu.find(b):
                return edges[i]
            dsu.union(a, b)
        
        return None