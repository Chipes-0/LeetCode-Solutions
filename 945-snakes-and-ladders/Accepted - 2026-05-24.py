class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        #bfs
        N = len(board)
        board = board[::-1]

        def getcell(num):
            row = (num - 1) // N
            col = (num - 1) % N
            if row % 2:
                col = N - 1 - col
            return board[row][col]

        queue = [(1, 0)]
        visited = [False] * ((N*N) + 1)

        while queue:
            curr, rolls = queue.pop(0)
            visited[curr] = True
            if curr >= N*N:
                return rolls
            for i in range(1, 7):
                next_cell = curr + i
                if visited[next_cell]:
                    continue

                if next_cell >= N*N:
                    return rolls + 1
                if getcell(next_cell) != -1:
                    next_cell = getcell(next_cell)
                visited[next_cell] = True
                queue.append((next_cell, rolls + 1))
        return -1