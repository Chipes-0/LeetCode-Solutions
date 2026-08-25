from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [0] * n
        ps = [0] * (n + 1)
        for i in range(n):
            ps[i + 1] = ps[i] + stones[i]
        
        dp[-1] = ps[n]
        for i in range(n - 2, -1, -1):
            val = ps[i + 1] - dp[i + 1]
            dp[i] = max(dp[i + 1], val)
        return dp[1]