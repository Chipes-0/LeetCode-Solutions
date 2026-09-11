from ast import List
from collections import Counter

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        c = Counter(digits)
        out = 0
        for i in range(100, 1000):
            d1 = i // 100
            d2 = (i // 10) % 10
            d3 = i % 10

            c[d1] -= 1
            c[d2] -= 1
            c[d3] -= 1
            if c[d1] >= 0 and c[d2] >= 0 and c[d3] >= 0 and d3 % 2 == 0:
                out += 1
            c[d1] += 1
            c[d2] += 1
            c[d3] += 1 
        return out