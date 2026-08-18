from collections import defaultdict
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = defaultdict(int)

        def step(stair: int):
            if stair in [0, 1]:
                return cost[stair]
            if stair in cache:
                return cache[stair]
            v1, v2 = step(stair - 1) + cost[stair], step(stair - 2) + cost[stair]
            cache[stair] = min(v1, v2)
            return cache[stair]

        return min(step(len(cost) - 1), step(len(cost) - 2))
        