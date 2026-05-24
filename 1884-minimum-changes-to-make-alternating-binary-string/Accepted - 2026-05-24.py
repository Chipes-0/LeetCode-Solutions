from collections import Counter

class Solution:
    def minOperations(self, s: str) -> int:
        c = Counter(s)
        return abs(c['0'] - c['1']) // 2        