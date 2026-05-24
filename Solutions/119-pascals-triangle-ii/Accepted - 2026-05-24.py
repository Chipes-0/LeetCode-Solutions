class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascaltriangle = [[1], [1, 1]]
        while len(pascaltriangle) < rowIndex + 1:
            row = [1]
            for i in range(1, len(pascaltriangle[-1])):
                row.append(pascaltriangle[-1][i] + pascaltriangle[-1][i - 1])
            row.append(1)
            pascaltriangle.append(row)
        return pascaltriangle[rowIndex]
        