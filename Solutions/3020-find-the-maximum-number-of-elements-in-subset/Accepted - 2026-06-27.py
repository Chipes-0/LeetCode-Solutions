from collections import Counter, defaultdict
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        c = Counter(nums)
        dd = defaultdict(int, c)
        # 1 2 4 8 16 8 4 2 1
        values = sorted(list(c.keys()))
        if 1 in values:
            values.remove(1)
        # pows = [1, 2, 4, 8, 16]
        out = 1
        for val in values:
            val_pows = []
            for i in range(5):
                val_pows.append(val)
                val = val * val
                if val > 1e9:
                    break
            size = 1
            for num in val_pows:
                if not dd[num]:
                    break
                if dd[num] >= 1:
                    out = max(out, size)
                if dd[num] >= 2:
                    size += 2
                
        
        ones = dd[1] if dd[1] % 2 == 1 else dd[1] - 1
        return max(out, ones)
