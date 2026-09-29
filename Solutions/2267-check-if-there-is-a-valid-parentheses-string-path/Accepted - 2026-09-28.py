class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        N, M = len(grid), len(grid[0])
        max_balance = N + M - 1
        dp = [[[False for _ in range(max_balance + 1)] for _ in range(M)] for _ in range(N)]
        if grid[0][0] == ")":
            return False
        dp[0][0][1] = True
        for i in range(N):
            for j in range(M):
                for balance in range(max_balance + 1):
                    if grid[i][j] == '(':
                        new_balance = balance + 1
                    else:
                        new_balance = balance - 1
                    
                    if new_balance < 0:
                        continue 
                    if i > 0 and dp[i - 1][j][balance]:
                        dp[i][j][new_balance] = True

                    if j > 0 and dp[i][j - 1][balance]:
                        dp[i][j][new_balance] = True
        return dp[N - 1][M - 1][0]