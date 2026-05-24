class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        res = [row[:] for row in grid]
        n, m = len(grid), len(grid[0])

        for i in range(x, x + k):
            new_i = x + (k - 1 - (i - x))
            for j in range(y, y + k):
                res[new_i][j] = grid[i][j]
        return res