from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return max(nums)
        if k == 1:
            nums = [x for x in nums if nums.count(x) == 1]
            if not nums:
                return -1
            return max(nums)
        
        val1, val2 = nums[0], nums[-1]
        if nums.count(val1) > 1:
            val1 = -1
        if nums.count(val2) > 1:
            val2 = -1
        return max(val1, val2)