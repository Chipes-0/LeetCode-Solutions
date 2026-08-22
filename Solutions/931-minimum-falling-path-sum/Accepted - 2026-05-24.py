class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N, M = len(matrix), len(matrix[0])
        cache = [[None] * N] * M
        def dfs(row, col):
            if row == M:
                return 0
            if col == M or col == - 1:
                return float("inf")
            ans = (matrix[row][col] + 
                min(dfs(row + 1, col - 1),
                    dfs(row + 1, col),
                    dfs(row + 1, col + 1)
            ))
            cache[row][col] = ans
            return ans
        matrix_min = float("inf")
        for i in range(N):
            matrix_min = min(dfs(0, i), matrix_min)
        return matrix_min