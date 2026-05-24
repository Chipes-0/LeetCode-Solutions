from collections import defaultdict

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        prefix_sum = [travel[0]]
        for i in range(1, len(travel)):
            prefix_sum.append(prefix_sum[-1] + travel[i])
        counters = defaultdict(int)
        last = defaultdict(int)
        for i in range(len(garbage)):
            for letter in garbage[i]:
                counters[letter] += 1
                last[letter] = i
        total = 0
        for l in ('G', 'M', 'P'):
            total += counters[l] 
            if last[l] != 0:
                total += prefix_sum[last[l] - 1]
        return total

