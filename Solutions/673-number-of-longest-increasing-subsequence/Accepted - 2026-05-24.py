from collections import Counter

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        nlen = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    val = dp[j] + 1
                    if val == dp[i]:
                        nlen[i] += 1
                    dp[i] = max(dp[i], val)
        m = max(dp)
        out = 0
        for i in range(len(dp)):
            if dp[i] == m:
                out += nlen[i]
        return out


