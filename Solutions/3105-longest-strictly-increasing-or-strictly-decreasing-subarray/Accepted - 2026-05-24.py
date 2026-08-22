class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        swi = 1
        swd = 1
        maxswi = 1
        maxswd = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                swi += 1
                swd = 1
            elif nums[i] < nums[i - 1]:
                swd += 1
                swi = 1
            else:
                swd = 1
                swi = 1
            maxswi = max(maxswi, swi)
            maxswd = max(maxswd, swd)
        return max(maxswi, maxswd)