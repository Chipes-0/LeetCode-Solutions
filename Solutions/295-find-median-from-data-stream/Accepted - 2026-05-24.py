class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        self.count = 0

    def addNum(self, num: int) -> None:
        self.count += 1
        if not self.maxHeap or num < -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else: 
            heapq.heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        

    def findMedian(self) -> float:
        if self.count & 1:
            return -self.maxHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()