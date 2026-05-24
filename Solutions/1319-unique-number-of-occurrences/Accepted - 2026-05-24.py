from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        unique = dict()

        for val in c.values():
            if val in unique:
                return False
            unique[val] = True
        return True