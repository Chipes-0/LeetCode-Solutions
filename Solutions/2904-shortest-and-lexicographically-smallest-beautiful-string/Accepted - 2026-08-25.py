class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        count = 0
        n = len(s)
        out = ""
        for right in range(n):
            if s[right] == "1":
                count += 1
            while count == k:
                candidate = s[left:right + 1]
                if not out or (len(candidate), candidate) < (len(out), out):
                    out = candidate
                if s[left] == "1":
                    count -= 1
                left += 1
        return out