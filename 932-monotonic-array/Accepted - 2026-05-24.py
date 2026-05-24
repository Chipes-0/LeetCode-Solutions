class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        monotone_dec = monotone_inc = True
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                monotone_dec = False
            if nums[i - 1] > nums[i]:
                monotone_inc = False
        return monotone_dec or monotone_inc