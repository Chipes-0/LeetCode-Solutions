class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n, m = len(mat), len(mat[0])

        def rotate(matrix):
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

            for i in range(n):
                matrix[i].reverse()

        def compare(mat):
            for i in range(n):
                for j in range(m):
                    if mat[i][j] != target[i][j]:
                        return False
            return True

        for _ in range(3):
            if compare(mat):
                return True
            rotate(mat)
        return False