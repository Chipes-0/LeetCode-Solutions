from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [abs(x) for x in nums]
        nums.sort()

        left = 0
        right = len(nums) - 1
        out = 0
        while left < right:
            out += (nums[right] ** 2) - (nums[left] ** 2)
            left += 1
            right -= 1
        if left == right:
            out += nums[left] ** 2
        return out