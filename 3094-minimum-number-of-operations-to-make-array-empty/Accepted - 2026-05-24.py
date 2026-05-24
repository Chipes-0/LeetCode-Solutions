from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        out = 0
        for val in c.values():
            if val == 1:
                return -1
            if val % 3 == 0:
                out += val // 3
            else:
                out += val // 3 + 1
        return out