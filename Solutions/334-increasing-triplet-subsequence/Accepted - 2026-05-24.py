class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        N = len(nums)
        dp = [1] * N
        for i in range(1, N):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > 2:
                        return True
        return False
