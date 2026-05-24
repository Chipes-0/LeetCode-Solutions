class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin, currMax, maxP = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            temp = max(nums[i], nums[i] * currMax, nums[i] * currMin)
            currMin = min(nums[i], nums[i] * currMax, nums[i] * currMin)
            currMax = temp

            maxP = max(maxP, currMax)
            
        return maxP