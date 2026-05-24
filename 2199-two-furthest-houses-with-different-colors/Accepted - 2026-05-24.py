class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        out = 0
        for i in range(n):
            for j in range(i + 1, n):
                if colors[i] != colors[j]:
                    out = max(out, j - i)
        return out