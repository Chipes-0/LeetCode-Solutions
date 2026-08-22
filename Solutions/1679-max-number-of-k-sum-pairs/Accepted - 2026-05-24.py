from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        out = 0
        d = defaultdict(int)
        for n in nums:
            if d[k-n]:
                out += 1
                d[k-n] -= 1
            else:
                d[n] += 1
        return out
