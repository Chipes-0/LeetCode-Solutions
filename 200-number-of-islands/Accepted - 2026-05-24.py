class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        N, M = len(grid), len(grid[0])
        def dfs(i, j):
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            if i < N - 1:
                dfs(i + 1, j)
            if j < M - 1:
                dfs(i, j + 1)


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count