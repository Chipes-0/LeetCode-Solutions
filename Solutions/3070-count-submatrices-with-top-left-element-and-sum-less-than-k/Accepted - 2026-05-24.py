class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        out = 0
        n, m = len(grid), len(grid[0])
        ps = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                ps[i][j] = ps[i - 1][j] + ps[i][ j -1] + grid[i - 1][j - 1] - ps[i - 1][j - 1]
                if ps[i][j] < k:
                    out += 1

        return out