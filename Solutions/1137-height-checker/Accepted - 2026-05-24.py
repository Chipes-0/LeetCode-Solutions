class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights2 = sorted(heights)
        out = 0
        for i in range(len(heights)):
            if heights[i] != heights2[i]:
                out += 1
        return out