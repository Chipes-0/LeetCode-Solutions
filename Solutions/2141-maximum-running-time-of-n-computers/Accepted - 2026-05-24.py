class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        if n == 1:
            return sum(batteries)
        if n > len(batteries):
            return 0
        return sum(batteries) // n