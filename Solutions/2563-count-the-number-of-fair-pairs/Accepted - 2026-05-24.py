class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        out = 0
        def bs(i, val):
            left, right = i, len(nums) -1
            while left <= right:
                m = left + (right - left) // 2
                if nums[m] >= val:
                    right = m - 1
                else:
                    left = m + 1
            return left

        for i, n in enumerate(nums):
            out += bs(i, upper - n + 1) - bs(i, lower - n) 
        return out
