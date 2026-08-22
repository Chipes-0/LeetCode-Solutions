from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
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
            
        dsu = DSU(n)
        arr = [(val, i) for i, val in enumerate(nums)]
        arr.sort()

        for i in range(n - 1):
            val1, j = arr[i]
            val2, k = arr[i + 1]

            if val2 - val1 <= maxDiff:
                dsu.union(j, k)
        
        out = []
        for query in queries:
            u, v = query
            out.append(dsu.find(u) == dsu.find(v))
        return out