class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        perimeter = 0
        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or not grid[r][c]:
                return 1
            if grid[r][c] == -1:
                return 0
            grid[r][c] = -1
            return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        

        for i in range(R):
            for j in range(C):
                if grid[i][j]:
                    return dfs(i, j)
        return 0
