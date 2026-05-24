class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        fc = defaultdict(list)
        out = []
        for x, y in c.items():
            fc[y].append(x)
        for i in range(1, 101):
            if len(out) == len(nums):
                break
            if i not in fc:
                continue
            if len(fc[i]) > 1:
                fc[i].sort(reverse = True)
            for element in fc[i]:
                for _ in range(i):
                    out.append(element)
        return out