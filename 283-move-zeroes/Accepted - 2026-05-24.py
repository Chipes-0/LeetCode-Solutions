class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[next_pos] = nums[i]
                next_pos += 1
            
        for i in range(next_pos, len(nums)):
            nums[i] = 0