import functools

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        res = functools.reduce(lambda a, b: a * b, nums)
        return 1 if res > 0 else 0 if res == 0 else -1