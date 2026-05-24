from collections import defaultdict
from math import comb

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [defaultdict(int) for _ in range(N)]
        for i in range(1, N):
            for j in range(0, i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1 + dp[j][diff]
        total = 0
        for i in range(N):
            total += sum(dp[i].values())
        total -= comb(N, 2)
        return total