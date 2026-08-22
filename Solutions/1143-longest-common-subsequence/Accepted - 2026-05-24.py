class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M =  len(text1), len(text2)
        dp = [[0] * (M + 1)] * (N + 1)
        for i in range(N + 1):
            for j in range(M + 1):
                print(i, j)
                if i == 0 or j == 0:
                    continue
                elif text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + max(dp[i - 1][j], dp[i][j - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) 
        return dp[N][M]