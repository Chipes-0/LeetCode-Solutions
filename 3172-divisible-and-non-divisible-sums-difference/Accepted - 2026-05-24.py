class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        out = 0
        for i in range(n + 1):
            if i % m == 0:
                out -= i
            else:
                out += i
        return out