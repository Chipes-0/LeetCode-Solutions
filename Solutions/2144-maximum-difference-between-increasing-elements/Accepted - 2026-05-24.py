class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        small = nums[0]
        out = -1
        for i in range(1, len(nums)):
            if nums[i] > small:
                out = max(nums[i] - small, out)
            else:
                small = nums[i]
        print(small)
        return out    
