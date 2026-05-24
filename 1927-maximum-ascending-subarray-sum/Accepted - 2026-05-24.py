class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        out = 0
        curr = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += nums[i]
            else:
                out = max(out, curr)
                curr = nums[i]
        return max(out, curr)