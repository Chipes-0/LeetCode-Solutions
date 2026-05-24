def getAllDivisors(num: int) -> int:
    divisors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisors += 1
    return divisors

class Solution:
    def bulbSwitch(self, n: int) -> int:
        bulbs = 0
        for i in range(1, n + 1):
            bulbs += 1 if getAllDivisors(i) % 2 == 1 else 0
        return bulbs
        