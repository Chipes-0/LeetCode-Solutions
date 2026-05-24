from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        c = Counter(nums)
        out = []
        for key in c:
            if len(out) < c[key]:
                for _ in range(c[key] - len(out)):
                    out.append([])
            for i in range(c[key]):
                out[i].append(key)
        return out