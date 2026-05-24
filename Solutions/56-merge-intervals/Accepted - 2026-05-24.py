class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        out = []
        start = intervals[0][0]
        end = intervals[0][1]
        for s, e in intervals[1:]:
            if s <= end:
                end = e
            else:
                out.append([start, end])
                start = s
                end = e
        out.append([start, end])
        return out