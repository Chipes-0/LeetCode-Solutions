class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in reversed(grid):
            for i in reversed(row):
                if i < 0:
                    count += 1
                else:
                    break
        return count