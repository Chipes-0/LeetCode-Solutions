from math import factorial
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter(nums)
        out = 0
        for val in c.values():
            if val >= 2:
                out += (val * (val - 1)) // 2
        return out