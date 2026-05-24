from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        out = []
        for i in range(k):
            out.append(max(d, key=d.get))
            del d[out[i]]
        return out