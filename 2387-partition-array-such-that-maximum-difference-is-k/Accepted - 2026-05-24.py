class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        out = 0
        small = nums[0]
        for num in nums:
            if small < num - k:
                out += 1
                small = num
        return out + 1