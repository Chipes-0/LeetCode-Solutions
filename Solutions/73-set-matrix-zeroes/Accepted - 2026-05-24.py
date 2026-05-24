class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    for ik in range(len(matrix)):
                        if matrix[ik][j]:
                            matrix[ik][j] = -1
                    for jk in range(len(matrix[0])):
                        if matrix[i][jk]:
                            matrix[i][jk] = -1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0