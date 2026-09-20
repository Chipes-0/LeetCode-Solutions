class Solution:
    def reverseDegree(self, s: str) -> int:
        out = 0

        for i in range(len(s)):
            out += (i + 1) * (26 - (ord(s[i]) - ord('a')))
        
        return out