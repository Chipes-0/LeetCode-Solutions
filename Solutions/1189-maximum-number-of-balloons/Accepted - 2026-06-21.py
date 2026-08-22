from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        out = float("inf")
        out = min(out, c['b'])
        out = min(out, c['a'])
        out = min(out, c['l']//2)
        out = min(out, c['o']//2)
        out = min(out, c['n'])
        
        return out