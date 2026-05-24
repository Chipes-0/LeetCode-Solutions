class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        out = [0] * len(nums)
        positive = 0
        negative = 1
        for i in range(len(nums)):
            if nums[i] < 0:
                out[negative] = nums[i]
                negative += 2
            else:
                out[positive] = nums[i]
                positive += 2
        return out