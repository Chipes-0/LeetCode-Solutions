class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [0] * n
        for i in range(n):
            out[i] = nums[nums[i]]
        return out