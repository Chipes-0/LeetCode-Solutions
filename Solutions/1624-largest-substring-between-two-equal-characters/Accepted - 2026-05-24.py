from collections import defaultdict

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {s[0]: 0}
        largest = float("-inf")
        for i in range(1, len(s)):
            if s[i] not in first:
                first[s[i]] = i
            else:
                largest = i - 1 - first[s[i]]
        return largest if largest > -1 else -1