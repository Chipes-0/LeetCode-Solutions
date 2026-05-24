class Solution:
    def scoreOfString(self, s: str) -> int:
        N = len(s) - 1
        out = 0
        for i in range(N ):
                out += abs(ord(s[i]) - ord(s[i + 1])) 
        return out