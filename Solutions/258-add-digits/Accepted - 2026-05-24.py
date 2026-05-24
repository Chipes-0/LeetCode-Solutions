def recSum(num: int):
    if num == 0:
        return num
    return num % 10 + recSum(num // 10)

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 10:
            num = recSum(num)
        return num