from collections import defaultdict

class Solution:
    def tribonacci(self, n: int) -> int:
        cache = defaultdict(int)

        def fibo(n: int) -> int:
            if n in [0, 1]:
                return n
            elif n == 2:
                return 1
            if n in cache:
                return cache[n]
            cache[n] = fibo(n - 1) + fibo(n - 2) + fibo(n - 3)
            return cache[n]
        return fibo(n)