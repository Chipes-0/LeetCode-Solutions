from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = defaultdict(int)
        left = 0
        out = 0
        for right in range(len(s)):
            ch = s[right]
            count[ch] += 1
            while left < right and count[ch] > 2:
                lch = s[left]
                count[lch] -= 1
                left += 1
            out = max(out, right - left + 1)
        return out