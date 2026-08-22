def lst(stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        if len(stones) == 0:
            return 0
        max1 = max(stones)
        stones.remove(max1)
        max2 = max(stones)
        stones.remove(max2)
        
        if max1 > max2:
            stones.append(max1 - max2)
        return lst(stones)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        return lst(stones)