class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        out = 0
        max_diag = 0
        for rec in dimensions:
            diag = math.sqrt(rec[0] * rec[0] + rec[1] * rec[1])
            if diag > max_diag:
                max_diag = diag
            if max_diag == diag:
                out = max(rec[0] * rec[1], out)
        return out