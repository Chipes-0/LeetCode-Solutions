from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:  
        frecuency = Counter(s)
        heap = []
        out = ""
        for value in frecuency.items():
            heapq.heappush(heap, (value[1] * - 1, value[0]))
        
        while len(heap) > 1:
            pop1, pop2 = heapq.heappop(heap), heapq.heappop(heap)
            out += pop1[1] + pop2[1]
            if pop1[0] != -1:
                heapq.heappush(heap, (pop1[0] + 1, pop1[1]))
            if pop2[0] != -1:
                heapq.heappush(heap, (pop2[0] + 1, pop2[1]))
        
        if heap:
            last = heapq.heappop(heap)
            if last[0] != -1:
                out = ""
            else:
                out += last[1]
        return out      
        