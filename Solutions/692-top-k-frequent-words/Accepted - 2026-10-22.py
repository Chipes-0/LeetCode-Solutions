from collections import Counter

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        c = Counter(words)
        arr = [(value, key) for key, value in c.items()]
        arr.sort(key=lambda x: (-x[0], x[1]))

        return [x[1] for x in arr[:k]]