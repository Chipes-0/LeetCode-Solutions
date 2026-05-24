class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {}
        sorted_arr = sorted(arr)
        pos = 1
        for n in sorted_arr:
            if n not in d:
                d[n] = pos
                pos += 1
        return [d[n] for n in arr]