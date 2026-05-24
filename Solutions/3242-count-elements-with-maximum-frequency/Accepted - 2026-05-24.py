from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        c2 = Counter(c.values())
        c2 = dict(reversed(sorted(c2.items())))
        for key, value in c2.items():
            return key * value
        return 0