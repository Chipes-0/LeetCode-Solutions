class Solution:
    def countCommas(self, n: int) -> int:
        out = 0
        coma = 1000
        while coma <= n:
            out += n - coma + 1
            coma *= 1000
        return out
