from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        N, M = len(classroom), len(classroom[0])

        Lcount = 0
        for i in range(N):
            for j in range(M):
                if classroom[i][j] == "S":
                    start = (i, j)
                elif classroom[i][j] == "L":
                    Lcount += 1
        if not Lcount:
            return 0
        pending = (1 << Lcount) - 1
        def BFS(x, y):
            queue = []
            # visited[r][c][energy][mask]
            seen = [[[[False] * (1 << pending  + 1) for _ in range(energy + 1)] for _ in range(M)] for _ in range(N)]
            start = (x, y, pending, energy, 0)
            seen[x][y][pending][energy] = True

            while queue:
                curr_x, curr_y, mask, e, steps = queue.pop(0)
