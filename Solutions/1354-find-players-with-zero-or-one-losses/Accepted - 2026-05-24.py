from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lossers = [item[1] for item in matches]
        set0 = set(item[0] for item in matches)
        set1 = set(lossers)
        set0 = set0.difference(set1)
        lose1 = [num for num in set1 if lossers.count(num) == 1]

        return [sorted(list(set0)),sorted(lose1)]