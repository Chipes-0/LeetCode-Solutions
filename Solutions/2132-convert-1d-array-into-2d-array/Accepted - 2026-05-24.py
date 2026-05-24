class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        out = []
        if m * n != len(original):
            return out
        for i in range(m):
            out.append(original[i*n : (i+1) *n])
        return out