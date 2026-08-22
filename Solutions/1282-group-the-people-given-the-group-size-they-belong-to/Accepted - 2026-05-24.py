from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        for index, item in enumerate(groupSizes):
            d[item].append(index)
        out = []
        for key, value in d.items():
            if key >= len(value):
                out.append(value)
            else:
                while len(value) >= key:
                    out.append(value[:key])
                    value = value[key:]
        return out