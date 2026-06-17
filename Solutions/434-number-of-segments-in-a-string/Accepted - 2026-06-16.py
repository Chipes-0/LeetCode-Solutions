class Solution:
    def countSegments(self, s: str) -> int:
        if not s:
            return 0
        out = 0
        if s[0] != " ":
            out += 1
        for i in range(len(s) - 1):
            if s[i] == " " and s[i + 1] != " ":
                out += 1
        return out