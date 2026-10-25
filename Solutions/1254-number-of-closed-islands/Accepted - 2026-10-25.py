class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        N, M = len(grid), len(grid[0])
        seen = [[False for _ in range(M)] for _ in range(N)]
        out = 0

        def bfs(i, j):
            dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            
            queue = [(i, j)]
            seen[i][j] = True
            flag = True
            
            while queue:
                x, y = queue.pop(0)
                for dx, dy in dirs:
                    newx, newy = x + dx, y + dy
                    if newx < 0 or newx >= N or newy < 0 or newy >= M:
                        continue
                    if seen[newx][newy]:
                        continue
                    if (newy in (0, M - 1) or newx in (0, N - 1)) and grid[newx][newy] == 0:
                        flag = False
                    if grid[newx][newy] == 0:
                        seen[newx][newy] = True
                        queue.append((newx, newy))
            
            if flag:
                return 1
            return 0

        for i in range(1, N - 1):
            for j in range(1, M - 1):
                if grid[i][j] == 0 and not seen[i][j]:
                    out += bfs(i, j)
        return out