class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        out = []
        cols = set()
        diag1 = set()
        diag2 = set()

        def validState(i, j):
            if j in cols:
                return False
            if (i + j) in diag1 or (i - j) in diag2:
                return False
            return True

        def backtracking(i):
            if i == n:
                out.append(["".join(row) for row in board])
                return 
            for j in range(n):
                if validState(i, j):
                    cols.add(j)
                    diag1.add(i + j)
                    diag2.add(i - j)
                    board[i][j] = "Q"
                    backtracking(i + 1)

                    board[i][j] = "."
                    cols.remove(j)
                    diag1.remove(i + j)
                    diag2.remove(i - j)
        backtracking(0)
        return out