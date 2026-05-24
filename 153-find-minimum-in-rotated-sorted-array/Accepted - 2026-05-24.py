class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        while left < right:
            m = (left + right) // 2
            print(nums[m])
            if nums[m] > nums[0]:
                left = m + 1
            else:
                right = m - 1
        if left >= len(nums):
            return nums[0]
        return nums[left]