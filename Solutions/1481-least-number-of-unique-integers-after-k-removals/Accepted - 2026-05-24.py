from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        c = {k: v for k, v in sorted(c.items())}
        removed = 0
        for key, value in c.items():
            if value <= k:
                removed += 1
                k -= value
            else:
                break           
        return len(c.items()) - removed