class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        out = 0
        for i in range(len(g)):
            if s[i] >= g[i] and i < len(s):
                out += 1
            else:
                break
        return out