class Solution:
    def makeFancyString(self, s: str) -> str:
        out = s[0:2]
        for l in s[2:]:
            if l == out[-1] and l == out[-2]:
                continue
            out += l
        return out