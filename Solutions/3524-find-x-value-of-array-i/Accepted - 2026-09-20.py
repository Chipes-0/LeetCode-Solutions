from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        dp = [[0 for _ in range(k)] for _ in range(N)]
        for i in range(N):
            val = nums[i] % k
            dp[i][val] = 1
            for x in range(k):
                val = (nums[i] * x) % k
                if i - 1 >= 0:
                    dp[i][val] += dp[i - 1][x]
        
        out = [0] * k

        for i in range(k):
            for j in range(N):
                out[i] += dp[j][i]
        return out