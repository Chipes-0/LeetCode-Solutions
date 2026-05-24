import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = heapq.heapify(nums)
        for i in range(len(nums) - k):
            out = heapq.heappop(nums)
        out = heapq.heappop(nums)
        return out