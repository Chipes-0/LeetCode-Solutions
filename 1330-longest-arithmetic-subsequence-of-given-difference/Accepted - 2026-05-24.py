from collections import defaultdict

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d = defaultdict(int)
        for a in arr:
            k = a - difference
            d[a] = d[k] + 1
        return max(d.values())
