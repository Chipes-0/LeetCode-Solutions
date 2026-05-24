class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        flag = n & 1
        n //= 2
        while n != 0:
            if n & 1 == flag:
                return False
            flag = n & 1
            n //= 2
        return True