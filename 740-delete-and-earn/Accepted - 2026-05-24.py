from collections import defaultdict

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        top_limit = float("-inf")
        bottom_limit = float("inf")
        for num in nums:
            counter[num] += num
            if num < bottom_limit:
                bottom_limit = num
            if num > top_limit:
                top_limit = num
        if len(counter.keys()) == 1:
            return counter[bottom_limit]
        if len(counter.keys()) == 2:
            return max(counter[bottom_limit], counter[top_limit])
        dp = defaultdict(int)
        dp[bottom_limit] = counter[bottom_limit]
        dp[bottom_limit + 1] = max(counter[bottom_limit], counter[bottom_limit + 1])

        for i in range(bottom_limit + 2, top_limit + 1):
            if i in counter:
                dp[i] = max(dp[i - 1], dp[i - 2] + counter[i])
        return dp[top_limit]
         