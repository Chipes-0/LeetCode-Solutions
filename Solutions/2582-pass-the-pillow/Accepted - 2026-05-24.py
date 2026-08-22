class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        rounds = (time // (n - 1)) % 2
        turns =  time % (n-1)
        return n - turns if rounds else turns + 1 