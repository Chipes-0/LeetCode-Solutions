class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        ps = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        px = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        out = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                num = 0
                isX = 0
                if grid[i - 1][j - 1] == "X":
                    num = 1
                    isX = 1
                elif grid[i - 1][j - 1] == "Y":
                    num = - 1
                ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] + num
                px[i][j] = px[i - 1][j] + px[i][j - 1] - px[i - 1][j - 1] + isX
                if ps[i][j] == 0 and px[i][j] > 0:
                    out += 1

        return out