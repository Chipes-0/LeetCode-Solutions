class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        sum_pairs = []
        nums = sorted(nums)
        total = len(nums)
        for i in range(total // 2):
            sum_pairs.append(nums[i] + nums[total - 1 - i])
        return max(sum_pairs)