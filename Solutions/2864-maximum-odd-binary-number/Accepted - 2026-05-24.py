class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = ''.join(sorted(s))
        s = s[:-1]
        return ''.join(reversed(s)) + "1"
