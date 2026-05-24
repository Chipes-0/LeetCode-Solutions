class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def validState(i, j, n):
            if i < 3:
                down, up = 0, 3
            elif i < 6:
                down, up = 3, 6
            elif i < 9:
                down, up = 6, 9
            if j < 3:
                left, right = 0, 3
            elif j < 6:
                left, right = 3, 6
            elif j < 9:
                left, right = 6, 9
            for k in range(9):
                if (board[i][k] == str(n) or
                    board[k][j] == str(n)):
                    return False
            for k1 in range(down, up):
                for k2 in range(left, right):
                    if board[k1][k2] == str(n):
                        return False
            return True
        
        def backtrack(i, j, sudoku):
            if j == 9:
                i += 1
                j = 0
            if i == 9:
                return True
            if sudoku[i][j] == ".":
                for n in range(1, 10):
                    if validState(i, j, n):
                        sudoku[i][j] = str(n)
                        if backtrack(i, j + 1, sudoku):
                            return True
                        sudoku[i][j] = "."
                return False
            else:
                return backtrack(i, j + 1, sudoku)
        backtrack(0, 0, board)