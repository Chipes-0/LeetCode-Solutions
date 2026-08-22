import math
from typing import List

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        n = len(nums)
        mx = nums[0]
        prefixGcd = [nums[0]]
        for i in range(1, n):
            mx = max(nums[i], mx)
            prefixGcd.append(math.gcd(mx, nums[i]))
        prefixGcd.sort()
        pairs = n // 2
        out = 0
        for i in range(pairs):
            out += math.gcd(prefixGcd[i], prefixGcd[n - 1 - i])
        return out
