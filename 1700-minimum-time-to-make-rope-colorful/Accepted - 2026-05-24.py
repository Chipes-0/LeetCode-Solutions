class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        current_max = neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                if neededTime[i] > current_max:
                    total += current_max
                    current_max = neededTime[i]
                else:
                    total += neededTime[i]
            else:
                current_max = neededTime[i]
        return total