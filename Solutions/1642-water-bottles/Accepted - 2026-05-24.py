class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        out = 0
        while numBottles >= numExchange:
            n = numBottles // numExchange
            out += numExchange * n

            numBottles -= numExchange * n
            numBottles += n
        return out + numBottles