from typing import List
from functools import cache

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        ps = [0] * (n + 1)
        for i in range(n):
            ps[i + 1] = ps[i] + stoneValue[i]
        
        @cache
        def dp(left, right):
            if left == right:
                return 0
            
            total = ps[right + 1] - ps[left]
            out = 0
            for i in range(left, right):
                suml = ps[i + 1] - ps[left]
                sumr = total - suml
                if suml < sumr:
                    out = max(out, dp(left, i) + suml)
                elif suml > sumr:
                    out = max(out, dp(i + 1, right) + sumr)
                else:
                    out = max(out, dp(left, i) + suml, dp(i + 1, right) + sumr)
            return out
        
        return dp(0, n - 1)
