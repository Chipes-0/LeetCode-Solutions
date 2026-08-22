class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        prefix_sum = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        out = -1
        print(nums)
        print(prefix_sum)
        for i in range(2, len(nums)):
            if prefix_sum[i - 1] > nums[i]:
                out = prefix_sum[i]
        return out