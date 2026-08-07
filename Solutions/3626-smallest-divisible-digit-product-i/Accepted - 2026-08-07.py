class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digitsP(n):
            p = 1
            while n:
                p *= n % 10
                n //= 10
            return p
        
        num = n
        while digitsP(num) % t != 0:
            num += 1
        return num