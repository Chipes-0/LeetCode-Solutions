class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        hm = defaultdict(list)
        s = set()
        out = -1
        for i, n in enumerate(nums):
            s.add(n)
            hm[n].append(i)
        for element in s:
            if len(hm[element]) < 3:
                pass
            idxs = hm[element]
            for i in range(len(idxs) - 2):
                val = 2 * (max(idxs[i: i + 3]) - min(idxs[i: i + 3]))
                if out == -1:
                    out = val
                else:
                    out = min(val, out)
        return out
                