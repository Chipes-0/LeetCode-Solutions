class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)

        while left <= right:
            m = (left + right) // 2
            if matrix[m][0] == target:
                return True
            if matrix[m][0] > target:
                right = m - 1
            else:
                left = m + 1

        left2 = 0
        right2 = len(matrix[right])
        while left2 <= right2:
            m = (left2 + right2) // 2
            if matrix[right][m] == target:
                return True
            if matrix[right][m] > target:
                right2 = m - 1
            else:
                left2 = m + 1
        print(matrix[right][right2])
        return matrix[right][right2] == target