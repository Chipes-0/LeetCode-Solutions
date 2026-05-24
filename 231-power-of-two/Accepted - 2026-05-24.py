import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return int(math.log(n, 2)) == math.log(n, 2)