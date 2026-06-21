from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        max_bars = 0
        freqCount = [0] * (max_cost + 1)
        for c in costs:
            freqCount[c] += 1
        for i in range(1, len(freqCount)):
            if not freqCount[i]:
                continue
            if coins >= i:
                count = min(freqCount[i], coins // i)
                coins -= count * i
                max_bars += count
            else:
                return max_bars
        return max_bars
        