class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        N = len(nums)
        for i in range(1, N):
            if nums[i] == nums[i - 1]:
                repeated = nums[i]
                break
        
        totalsum = N * (N + 1) / 2
        actualsum = sum(nums)
        return [repeated, int(totalsum - actualsum + repeated)]

