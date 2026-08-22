class Solution:
    def minChanges(self, s: str) -> int:
        out = 0
        for i in range(1, len(s), 2):
            if s[i-1:i +1] != "11" and s[i-1:i +1] != "00":
                out += 1
        return out