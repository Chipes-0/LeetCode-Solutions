class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        index = 0
        for i in range(len(nums)):
            if nums[i] & 1 == 0:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
        return nums