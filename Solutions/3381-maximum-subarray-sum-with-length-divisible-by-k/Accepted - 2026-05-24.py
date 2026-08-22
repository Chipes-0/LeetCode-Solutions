class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        out = float("-inf")
        og_k = k
        while k <= len(nums):
            window_sum = 0
            for i in range(k):
                window_sum += nums[i]
            if window_sum > out:
                out = window_sum
            
            for i in range(k, len(nums)):
                window_sum += nums[i] - nums[i - k]
                if window_sum > out:
                    out = window_sum
            k += og_k
        return out