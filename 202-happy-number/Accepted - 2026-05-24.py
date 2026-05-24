class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        if n > 9:
            n = sum(int(digit) ** 2 for digit in str(n))
            print(n)
            return self.isHappy(n)
        else:
            return False