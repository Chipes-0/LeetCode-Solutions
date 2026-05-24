class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        N, M = len(grid), len(grid[0])
        visited = [[False]*M for _ in range(N)]
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(y, x, py, px):
            visited[y][x] = True

            for dy, dx in dirs:
                ny, nx = y + dy, x + dx

                if ny < 0 or ny >= N or nx < 0 or nx >= M:
                    continue
                if grid[ny][nx] != grid[y][x]:
                    continue

                if not visited[ny][nx]:
                    if dfs(ny, nx, y, x):
                        return True
                elif (ny, nx) != (py, px):
                    return True  

            return False

        for i in range(N):
            for j in range(M):
                if not visited[i][j]:
                    val = dfs(i, j, None, None)
                    if val:
                        return True
        return False