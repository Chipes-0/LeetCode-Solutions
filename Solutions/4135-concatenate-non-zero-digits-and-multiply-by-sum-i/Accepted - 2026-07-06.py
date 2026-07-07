class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n = [x for x in list(str(n)) if x != "0"]
        val = 0
        suma = 0
        for num in n:
            val *= 10
            val += int(num)
            suma += int(num)
        return val * suma