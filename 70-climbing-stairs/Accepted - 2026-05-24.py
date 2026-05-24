class Solution:
    def climbStairs(self, n: int) -> int:
        def countWays(n: int) -> int:
            nonlocal x
            if n in [1, 2]: return n
            x += countWays(n - 1) + countWays(n - 2)
            return x
        x = 0
        return countWays(n)