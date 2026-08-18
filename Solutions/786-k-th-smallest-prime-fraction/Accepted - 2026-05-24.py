import heapq
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        start = 0
        end = len(arr) - 1
        for i in range(end + 1):
            heapq.heappush(heap, (arr[i] / arr[end], i, end))
        
        for _ in range(k - 1):
            val, num, deno = heapq.heappop(heap)
            deno -= 1
            if deno > num:
                heapq.heappush(heap, (arr[num] / arr[deno], num, deno))
        _, a, b = heapq.heappop(heap)
        return [arr[a], arr[b]]