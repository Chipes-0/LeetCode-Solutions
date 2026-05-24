from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        heap = []
        for key, value in c.items():
            heappush(heap, (-value, key))
        out = ""
        while heap:
            pop = heappop(heap)
            out += -pop[0] * pop[1]
        return out