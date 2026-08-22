class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def max_33(i, j):
            actual_max = 1
            for i2 in (i - 1, i, i + 1):
                for j2 in (j - 1, j, j + 1):
                    actual_max = max(actual_max, grid[i2][j2])
            return actual_max
        out = []
        for i in range(1, len(grid) - 1):
            out.append([])
            for j in range(1, len(grid) - 1):
                out[-1].append(max_33(i, j))
        return out