from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        intervals = [[start, end, weight, index] for index, (start, end, weight) in enumerate(intervals)]
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)

        def bs(val):
            left, right = 0, n
            out = -1
            while left < right:
                m = (left + right) // 2
                if intervals[m][1] < val:
                    out = m
                    left = m + 1
                else:
                    right = m
            return left

        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        for k in range(1, 5):
            for i in range(1, n + 1):
                start, end, weight, idx = intervals[i - 1]
                j = bs(start)
                skip = dp[i - 1][k]
                take = dp[j][k - 1]

                if skip[0] > take[0] + weight:
                    dp[i][k] = (skip[0], skip[1])
                elif skip[0] < take[0] + weight:
                    dp[i][k] = (take[0] + weight, sorted(take[1] + [idx]))
                else:
                    dp[i][k] = (skip[0], min(skip[1], sorted(take[1] + [idx])))


        if dp[n][4][1] == [0, 0, 0, 0]:
            return [0]
        return dp[n][4][1]