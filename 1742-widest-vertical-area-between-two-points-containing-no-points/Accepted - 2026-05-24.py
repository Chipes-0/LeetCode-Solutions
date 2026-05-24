class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[0])
        out = float("-inf")
        for i in range(1, len(points)):
            dif = points[i][0] - points[i - 1][0]
            if dif > out:
                out = dif
        return out
        