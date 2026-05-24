import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        out = [0] * len(score)
        score = [(-x, i) for i, x in enumerate(score)]
        heapq.heapify(score)
        i = 0
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        while score:
            n = heapq.heappop(score)
            if i < 3:
                out[n[1]] = medals[i]
            else:
                out[n[1]] = str(i + 1)
            i += 1
        return out