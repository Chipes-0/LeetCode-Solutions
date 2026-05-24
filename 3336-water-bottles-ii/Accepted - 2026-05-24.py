class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        out = 0
        empty = 0
        while numBottles or empty >= numExchange:
            if empty >= numExchange:
                empty -= numExchange
                numBottles += 1
                numExchange += 1
            else:
                out += numBottles
                empty += numBottles
                numBottles = 0
        return out