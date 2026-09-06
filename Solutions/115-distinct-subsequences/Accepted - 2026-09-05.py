class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N, M = len(s), len(t)

        dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
        for i in range(N):
            dp[i][0] = 1

        #   " a b c
        # " 1 0 0 0
        # a 1 1 0 0
        # b 1 1 1 0
        # b 1 1 2 0
        # c 1 1 2 2

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                dp[i][j] += dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[N][M]
        
