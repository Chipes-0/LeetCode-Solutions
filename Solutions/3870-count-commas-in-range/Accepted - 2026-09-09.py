class Solution:
    def countCommas(self, n: int) -> int:
        out = 0
        if n < 1000:
            return out
        
        return n - 999