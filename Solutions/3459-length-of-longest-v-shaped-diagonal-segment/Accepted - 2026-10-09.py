from typing import List

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        dp = [[[[0 for _ in range(2)] for _ in range(4)] for _ in range(M)] for _ in range(N)]
        seq = {1: 2, 2: 0, 0: 2}

        # x, y
        dirs = [
            (1, 1), # derecha abajo
            (-1, 1), # izquierda abajo
            (-1, -1), # izquierda arriba
            (1, -1) # derecha arriba
        ]


        for d, (dj, di) in enumerate(dirs):
            rows = range(N) if di == 1 else range(N - 1, -1, -1)
            cols = range(M) if dj == 1 else range(M - 1, -1, -1)

            for i in rows:
                for j in cols:
                    if grid[i][j] == 1:
                        dp[i][j][d][0] = 1

                    cur = dp[i][j][d][0]
                    if cur == 0:
                        continue
                    ## Recto
                    ni, nj = i + di, j + dj
                    if (0 <= ni < N and 0 <= nj < M) and grid[ni][nj] == seq[grid[i][j]]:
                        dp[ni][nj][d][0] = max(dp[ni][nj][d][0], cur + 1)

                    ## Girar
                    izq = (d + 1) % 4
                    ni, nj = i + dirs[izq][1], j + dirs[izq][0]
                    if (0 <= ni < N and 0 <= nj < M) and grid[ni][nj] == seq[grid[i][j]]:
                        dp[ni][nj][izq][1] = max(dp[ni][nj][izq][1], cur + 1)
        
        for d, (dj, di) in enumerate(dirs):
            rows = range(N) if di == 1 else range(N - 1, -1, -1)
            cols = range(M) if dj == 1 else range(M - 1, -1, -1)
            for i in rows:
                for j in cols:
                    cur = dp[i][j][d][1]
                    if cur == 0:
                        continue
                    ## Recto
                    ni, nj = i + di, j + dj
                    if (0 <= ni < N and 0 <= nj < M) and grid[ni][nj] == seq[grid[i][j]]:
                        dp[ni][nj][d][1] = max(dp[ni][nj][d][1], cur + 1)
        
        out = 0
        for i in range(N):
            for j in range(M):
                for k in range(4):
                    for l in range(2):
                        out = max(out, dp[i][j][k][l])
        return out
