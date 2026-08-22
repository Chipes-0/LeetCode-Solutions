class RecentCounter:

    def __init__(self):
        self.queue = []
        self.n = 0

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[-1] - 3000 > self.queue[0]:
            self.queue.pop(0)
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)