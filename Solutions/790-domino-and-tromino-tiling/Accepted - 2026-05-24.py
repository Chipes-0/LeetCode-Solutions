class Solution:
    def numTilings(self, n: int) -> int:
        dp = [1, 2, 5]
        modulo = 10**9 + 7
        if n < 4:
            return dp[n - 1]
        for i in range(n-3):
            dp[0], dp[1], dp[2] = dp[1], dp[2], dp[1] * 2 + dp[0]
        return dp[-1]