from collections import defaultdict
from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
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
        
        n = len(nums)
        dsu = DSU(n)
        arr = sorted((value, index) for index, value in enumerate(nums))
        for i in range(1, n):
            prev_value, prev_idx = arr[i - 1]
            curr_value, curr_idx = arr[i]

            if curr_value - prev_value <= limit:
                dsu.union(prev_idx, curr_idx)
        
        groups = defaultdict(list)
        for i, p in enumerate(dsu.parent):
            groups[p].append(nums[i])
        for key in groups:
            groups[key].sort()
        
        out = []
        for num in dsu.parent:
            out.append(groups[num].pop(0))
        return out
