class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        arrays.sort(key=lambda x:x[-1])
        return arrays[-1][-1] - arrays[0][0]