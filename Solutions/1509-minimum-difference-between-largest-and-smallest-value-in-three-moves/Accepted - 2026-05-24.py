class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums) < 3:
            return 0
        return nums[-4] - nums[0]