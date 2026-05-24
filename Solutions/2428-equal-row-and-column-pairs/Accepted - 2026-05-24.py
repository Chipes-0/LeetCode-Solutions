from collections import defaultdict

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = defaultdict(int)

        for i in range(len(grid)):
            s1 = ""
            s2 = ""
            for j in range(len(grid)):
                s1 += str(grid[j][i])
                s2 += str(grid[i][j])
            rows[s1] += 1
            rows[s2] += 1

        sum = 0
        for key in rows:
            if rows[key] > 1:
                sum += rows[key] - 1
        return sum