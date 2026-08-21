from typing import List
import math

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        m = 1 << n

        bits = [0] * m
        lcm = [0] * m

        for mask in range(1, m):
            clmc = 1
            for i, c in enumerate(coins):
                if mask & (1 << i):
                    clmc = math.lcm(clmc, c)
                    bits[mask] += 1
            lcm[mask] = clmc
        

        def count(x):
            out = 0
            for i in range(1, m):
                if bits[i] & 1:
                    out += x // lcm[i]
                else:
                    out -= x // lcm[i]
            return out

        left = k
        right = k * min(coins)

        while left < right:
            mid = (left + right) // 2
            val = count(mid)
            if val < k:
                left = mid + 1
            else:
                right = mid
        return left
