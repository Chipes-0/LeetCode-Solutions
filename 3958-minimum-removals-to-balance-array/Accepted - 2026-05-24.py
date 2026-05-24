class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        low = nums[0] * k
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] <= low:
                return len(nums) - i  -1
        return 0