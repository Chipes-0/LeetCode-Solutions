class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        sign = 1 if n > 0 else -1
        factor = x if n > 0 else 1/x
        while abs(n) > 0:
            ans *= factor
            n -= sign
            print(n)
        return ans
            