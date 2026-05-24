class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        out = 0
        for i in range(left, right + 1):
            binary = bin(i) 
            if binary.count("1") in primes:
                out += 1
        return out