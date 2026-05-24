class Solution:
    def longestPrefix(self, s: str) -> str:
        max_s = ""
        for i in range(len(s)):
            if s[:-i] == s[i:]:
                if max_s == "":
                    return s[i:]
        return max_s