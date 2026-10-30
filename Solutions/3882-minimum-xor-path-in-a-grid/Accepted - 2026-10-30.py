class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        N, M = len(grid), len(grid[0])
        dp = [[False for _ in range(1024)] for _ in range(M)]
        dp[0][grid[0][0]] = True

        for j in range(1, M):
            for x in range(1024):
                if dp[j - 1][x]:
                    val_left = x ^ grid[0][j]
                    dp[j][val_left] = True
        
        for i in range(1, N):
            for j in range(M):
                curr = [False] * 1024
                for x in range(1024):
                    if dp[j][x]:
                        up_val = x ^ grid[i][j]
                        curr[up_val] = True
                    
                    if j > 0 and dp[j - 1][x]:
                        left_val = x ^ grid[i][j]
                        curr[left_val] = True
                dp[j] = curr


        for i in range(1024):
            if dp[M - 1][i]:
                return i
        return -1