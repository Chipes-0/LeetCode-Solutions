class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        cache = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    cache[i][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if cache[i][j] != 0:
                    cache[i][j] = cache[i - 1][j] + cache[i][j - 1]
        
        return cache[m - 1][n - 1]