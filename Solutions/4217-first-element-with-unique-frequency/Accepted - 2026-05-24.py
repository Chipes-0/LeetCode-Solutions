class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        uniques = []
        firstap = {}
        c = defaultdict(int)
        freqs = defaultdict(list)

        for i, n in enumerate(nums):
            if n not in firstap:
                firstap[n] = i
            c[n] += 1
        
        for key, value in c.items():
            freqs[value].append(key)
        
        for key, value, in freqs.items():
            if len(value) == 1:
                uniques.append(value[0])

        if not uniques:
            return -1
        first = float("inf")
        out = None

        for n in uniques:
            if firstap[n] < first:
                first = firstap[n]
                out = n
        return out

            