class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        ps_h = [0] * (n + 1)
        ps_v = [0] * (m + 1)

        for i in range(n):
            row_sum = 0
            for j in range(m):
                val = grid[i][j]
                
                row_sum += val
                ps_v[j + 1] += val
            ps_h[i + 1] = ps_h[i] + row_sum
        for j in range(m):
            ps_v[j + 1] += ps_v[j]

        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            diff = ps_h[mid + 1] - 2 * ps_h[mid]
            if diff == 0:
                return True
            if diff < 0:
                right = mid - 1
            else:
                left = mid + 1
        
        left, right = 0, m
        while left < right:
            mid = (left + right) // 2
            diff = ps_v[mid + 1] - 2 * ps_v[mid]
            if diff == 0:
                return True
            if diff < 0:
                right = mid - 1
            else:
                left = mid + 1
        return False