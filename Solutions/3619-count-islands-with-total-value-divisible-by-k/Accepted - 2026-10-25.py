from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        N, M = len(grid), len(grid[0])
        seen = [[False for _ in range(M)] for _ in range(N)]
        out = 0

        def bfs(i, j):
            dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            queue = [(i, j)]
            seen[i][j] = True
            value = 0

            while queue:
                x, y = queue.pop(0)
                value += grid[x][y]
                for dx, dy in dirs:
                    newx, newy = x + dx, y + dy
                    if newx < 0 or newx >= N or newy < 0 or newy >= M:
                        continue
                    if seen[newx][newy]:
                        continue
                    if grid[newx][newy]:
                        seen[newx][newy] = True
                        queue.append((newx, newy))
            return value
        
        out = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] and not seen[i][j]:
                    value = bfs(i, j)
                    if value % k == 0:
                        out += 1
        return out