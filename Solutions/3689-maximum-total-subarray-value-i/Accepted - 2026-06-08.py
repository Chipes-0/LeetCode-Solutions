class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        val = max(nums) - min(nums)
        return val * k