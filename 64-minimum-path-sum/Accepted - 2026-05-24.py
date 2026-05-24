class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = (len(grid) + 1)
        m = (len(grid[0]) + 1)
        dp = [[1000 for _ in range(m)] for _ in range(n)] 
        for i in range(1, n):
            for j in range(1, m):
                val = grid[i - 1][j - 1]
                add = min(dp[i - 1][j], dp[i][j - 1])
                if  add == 1000:
                    add = 0
                dp[i][j] =  add + val
        for r in dp:
            print(r)
        return dp[n-1][m-1]
