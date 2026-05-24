class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        out = []
        for i in range(len(matrix)):
            min_row = float("inf")
            index = 0
            for j in range(len(matrix[i])):
                if matrix[i][j] < min_row:
                    min_row = matrix[i][j]
                    index = j
            flag = True
            for j in range(len(matrix)):
                if matrix[j][index] > min_row:
                    flag = False
                    break
            if flag:
                out.append(min_row)
        return out