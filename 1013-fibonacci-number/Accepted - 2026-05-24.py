from collections import defaultdict

class Solution:
    def fib(self, n: int) -> int:
        cache = defaultdict(int)

        def fibo(n: int) -> int:
            if n in [0, 1]:
                return n
            elif n in cache:
                return cache[n]
            else:
                cache[n] = fibo(n - 1) + fibo(n - 2)
            return cache[n]

        return fibo(n)