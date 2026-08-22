class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum)
        out = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                out[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= out[i][j]
                colSum[j] -= out[i][j]
        return out