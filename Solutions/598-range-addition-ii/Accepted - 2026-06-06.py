class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n

        for R, C in ops:
            for i in range(R):
                rows[i] += 1
            
            for i in range(C):
                cols[i] += 1

        return rows.count(rows[0]) * cols.count(cols[0])