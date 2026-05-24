class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        nums = sorted(c.values())
        odd = [x for x in nums if x % 2 == 1]
        even = [x for x in nums if x % 2 == 0]
        return max(odd[-1] - even[0], even[-1] - odd[0])