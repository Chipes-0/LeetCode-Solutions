from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def hasDuplicates(nums: List[str]) -> bool:
            counter = Counter(nums)
            return any(count > 1 for num, count in counter.items() if num != ".")

        for i in range(9):
            if hasDuplicates(board[i]):
                return False
            col = [board[i][j] for j in range(9)]
            if hasDuplicates(col):
                return False

        for i in range(3):
            for j in range(3):
                box = [board[x][y] for x in range(i * 3, (i*3) + 3) for y in range(j * 3, (j * 3) + 3)]
                if hasDuplicates(box):
                    return False

        return True