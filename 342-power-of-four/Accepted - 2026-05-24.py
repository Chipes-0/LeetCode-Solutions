import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        log = math.log(n, 4)
        return log == int(log)