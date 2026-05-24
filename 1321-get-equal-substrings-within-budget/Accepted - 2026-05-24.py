class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diffs = []
        for i in range(len(s)):
            num = abs(ord(s[i]) - ord(t[i]))
            diffs.append(num)
        left = 0
        window = 0
        out = 0
        for right in range(len(s)):
            window += diffs[right]
            while window > maxCost:
                window -= diffs[left]
                left += 1
            if (right - left + 1) > out:
                out = right - left + 1
        return out