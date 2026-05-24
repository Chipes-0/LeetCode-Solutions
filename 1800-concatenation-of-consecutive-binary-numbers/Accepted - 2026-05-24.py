class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MODULO = (10** 9) + 7

        out = 0
        for i in range(1, n + 1):
            bits = math.floor(math.log2(i)) + 1
            out *= math.pow(2, bits) 
            out += i 
        return int(out) % MODULO