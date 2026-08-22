class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        ## prefix sum de filas
        row_ps = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                row_ps[i][j] = grid[i][j] + (row_ps[i][j-1] if j > 0 else 0)

        ## prefix sum de columnas
        col_ps = [[0] * m for _ in range(n)]
        for j in range(m):
            for i in range(n):
                col_ps[i][j] = grid[i][j] + (col_ps[i-1][j] if i > 0 else 0)

        ## prefix sum de diagonales
        diag1_ps = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                diag1_ps[i][j] = grid[i][j] + (
                    diag1_ps[i-1][j-1] if i > 0 and j > 0 else 0
                )
        
        ## prefix sum de diagonales 
        diag2_ps = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m-1, -1, -1):
                diag2_ps[i][j] = grid[i][j] + (
                    diag2_ps[i-1][j+1] if i > 0 and j < m-1 else 0
                )
        
        out = 1
        max_box_size = min(n, m)

        for box in range(1, max_box_size + 1):
            for i in range(0, n - box + 1):
                for j in range(0, m - box + 1):

                    row_sum = row_ps[i][j + box - 1] - (row_ps[i][j - 1] if j > 0 else 0)
                    col_sum = col_ps[i + box - 1][j] - (col_ps[i - 1][j] if i > 0 else 0)
                    d1_sum = diag1_ps[i + box - 1][j + box - 1] - (
                        diag1_ps[i - 1][j - 1] if i > 0 and j > 0 else 0
                    )
                    d2_sum = diag2_ps[i + box - 1][j] - (
                        diag2_ps[i - 1][j + box] if i > 0 and j + box < m else 0
                    )
                    if row_sum == col_sum == d1_sum == d2_sum:
                        out = box

        return out