class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        res = [False] * n

        for i in range(n):
            for j in range(i + 1,  min(n, i + nums[i] + 1)):
                res[j] = True
        return res[-1]