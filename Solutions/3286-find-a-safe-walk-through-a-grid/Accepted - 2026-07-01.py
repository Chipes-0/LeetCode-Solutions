from typing import List
from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        N, M = len(grid), len(grid[0])
        INF = float("inf")
        dp = [[INF for _ in range(M)] for _ in range(N)]
        dp[0][0] = grid[0][0]
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dq = deque([(0, 0)])
        while dq:
            row, col = dq.popleft()
            for dx, dy in dirs:
                nrow = row + dy
                ncol = col + dx
                if 0 <= nrow < N and 0 <= ncol < M:
                    cost = grid[nrow][ncol]
                    new_damage = dp[row][col] + cost
                    if new_damage < dp[nrow][ncol]:
                        dp[nrow][ncol] = new_damage
                        if not cost:
                            dq.appendleft((nrow, ncol))
                        else:
                            dq.append((nrow, ncol))
        return dp[N - 1][M - 1] < health