class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        out = 0
        while cost:
            if len(cost) >= 3:
                out += cost.pop(-1)
                out += cost.pop(-1)
                cost.pop(-1)
            else:
                out += cost.pop(-1)
        return out