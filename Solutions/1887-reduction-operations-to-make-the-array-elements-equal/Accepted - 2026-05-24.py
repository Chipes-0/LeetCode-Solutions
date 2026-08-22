class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums = sorted(nums)[::-1]
        out = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                out += i
        return out 