from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        while left < right:
            m = (left + right) // 2
            if nums[m] > nums[-1]:
                left = m + 1
            else:
                right = m
        return nums[left]