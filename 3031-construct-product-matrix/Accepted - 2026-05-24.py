class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MODULO = 12345
        n, m = len(grid), len(grid[0])
        out = [[ 0 for _ in range(m)] for _ in range(n)]
        sufix = [1] * (n * m + 1)
        prefix = [1] * (n * m + 1)

        for i in range(n):
            for j in range(m):
                pos = 1 + (i * m) + j
                prefix[pos] = prefix[pos - 1] * grid[i][j] % MODULO
                sufix[pos] = sufix[pos - 1] * grid[n - 1 - i][m - 1 - j] % MODULO
        
        sufix = sufix[::-1]
        for i in range(n):
            for j in range(m):
                pos = (i * m) + j
                out[i][j] = prefix[pos] * sufix[pos + 1] % MODULO
        return out
        