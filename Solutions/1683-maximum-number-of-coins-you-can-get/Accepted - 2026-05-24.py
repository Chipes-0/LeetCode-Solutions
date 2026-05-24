class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        me = 0
        while piles:
            a, m, b = piles.pop(), piles.pop(), piles.pop(0)
            me += m
        return me