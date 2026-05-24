class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        out = 0
        start = points[0]
        points = points[1:]
        for next_point in points:
            while start[0] < next_point[0] and start[1] < next_point[1]:
                out += 1
                start[0] += 1
                start[1] += 1
            while start[0] > next_point[0] and start[1] < next_point[1]:
                out += 1
                start[0] -= 1
                start[1] += 1
            while start[0] > next_point[0] and start[1] > next_point[1]:
                out += 1
                start[0] -= 1
                start[1] -= 1
            while start[0] < next_point[0] and start[1] > next_point[1]:
                out += 1
                start[0] += 1
                start[1] -= 1
            
            if start == next_point:
                continue
            if start[0] != next_point[0]:
                out += abs(next_point[0] - start[0])
            else:
                out += abs(next_point[1] - start[1])
            start = next_point
        return out