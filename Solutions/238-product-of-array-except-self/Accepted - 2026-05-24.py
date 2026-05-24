import numpy

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n
        prefix = postfix = 1
        for i in range(1, n):
            prefix = out[i - 1] * nums[i- 1]
            out[i] = prefix
        for i in range(1, n + 1):
            out[n - i] = out[n - i] * postfix
            postfix = postfix * nums[n - i]
        return out
