class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                matrix[j].insert(n, matrix[i][j])

        for i in range(len(matrix)):
            matrix[i] = matrix[i][n::]
