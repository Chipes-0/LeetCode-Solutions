class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        modulo = 10 ** 9 + 7
        dp = [[0 for _ in range(n)] for _ in range(m)]
        def dfs(r, c, moves):
            if r < 0 or r == m:
                return 1
            if c < 0 or c == n:
                return 1
            if moves == 0:
                return 0
            dp[r][c] = dfs(r + 1, c, moves - 1) + dfs(r - 1, c, moves - 1) + dfs(r, c + 1, moves - 1) + dfs(r, c - 1, moves - 1)
            return dp[r][c]
        return dfs(startRow, startColumn, maxMove)