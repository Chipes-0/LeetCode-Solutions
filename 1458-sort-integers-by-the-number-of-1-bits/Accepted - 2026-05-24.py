from collections import Counter, defaultdict

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        df = defaultdict(list)
        for num in arr:
            c = Counter(bin(num)[2:])
            df[c['1']].append(num)
        out = []
        for key, value in df.items():
            out += sorted(value)
        return out