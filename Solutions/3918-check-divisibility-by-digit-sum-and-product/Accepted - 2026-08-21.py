class Solution:
    def checkDivisibility(self, n: int) -> bool:
        total = 0
        product = 1
        curr = n
        while curr:
            digit = curr % 10
            total += digit
            product *= digit
            curr //= 10
        return n % (total + product) == 0