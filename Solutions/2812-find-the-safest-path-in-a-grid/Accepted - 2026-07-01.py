from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        dist = [[-1] * M for _ in range(N)]

        queue = []
        for i in range(N):
            for j in range(M):
                if grid[i][j]:
                    queue.append((i, j))
                    dist[i][j] = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        topValue = 0
        while queue:
            x, y = queue.pop(0)
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if dist[nx][ny] == -1:
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx, ny))
                    topValue = max(topValue, dist[x][y] + 1)
                           
        def DFS(r, c, dist, value):
            nonlocal visited
            if dist[r][c] < value: 
                return False
            if r < 0 or r >= N or c < 0 or c >= M:
                return False
            if (r, c) in visited:
                return False
            if r == N - 1 and c == M - 1:
                return True
            visited.add((r, c))
            for dy, dx in dirs:
                nr, nc = r + dy, c + dx
                if nr < 0 or nr >= N or nc < 0 or nc >= M:
                    continue
                if dist[nr][nc] < value:
                    continue
                if DFS(nr, nc, dist, value):
                    return True
            return False
        
        left, right = 0, topValue
        ans = 0
        while left <= right:
            visited = set() 
            m = (left + right) // 2
            if DFS(0, 0, dist, m):
                ans = m
                left = m + 1
            else:
                right = m - 1
        return ans