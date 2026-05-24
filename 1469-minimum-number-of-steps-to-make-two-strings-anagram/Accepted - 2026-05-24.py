from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        N = len(s)
        c = Counter(s)
        count = 0
        for i in range(N):
            if t[i] in c and c[t[i]] > 0:
                c[t[i]] -= 1
                count += 1
        return N - count