class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        out = 0

        left = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            while curr_sum > k and left < right:
                curr_sum -= nums[left]
            if curr_sum == k:
                out += 1

        return out