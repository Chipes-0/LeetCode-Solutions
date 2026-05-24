class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        out = []
        left, right = 0, len(nums) - 1
        while left <= right:
            if abs(nums[right]) > abs(nums[left]):
                out.insert(0, nums[right] ** 2)
                right -= 1
            else:
                out.insert(0, nums[left] ** 2)
                left += 1
        return out
 

