class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        smallestLeft = float("inf")
        for i in range(1, len(prices)):
            smallestLeft = min(smallestLeft, prices[i - 1])
            out = max(prices[i] - smallestLeft, out)
        if out < 0:
            return 0
        return out 