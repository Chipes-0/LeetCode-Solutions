class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxcount = 0 
        current = 0
        previous = 0
        if 0 not in nums:
            return len(nums) - 1
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
            if nums[i] == 0 or i == len(nums) - 1:
                maxcount = max(maxcount, current + previous)
                previous, current = current, 0
                
        return maxcount