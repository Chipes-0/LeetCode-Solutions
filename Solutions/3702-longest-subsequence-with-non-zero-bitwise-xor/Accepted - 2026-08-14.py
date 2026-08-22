from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        nums.sort()
        for num in nums:
            total ^= num
        
        if total:
            return n
        if nums[0] == 0 and nums[-1] == 0:
            return 0
        return n - 1
