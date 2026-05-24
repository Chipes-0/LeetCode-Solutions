class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Ordenar lista de intervalos por orden de finalización
        intervals.sort(key=lambda x: x[1])
        remove = 0
        for i in range(1, len(intervals)):
            if intervals[i - 1][1] > intervals[i][0]:
                remove += 1
        return remove
