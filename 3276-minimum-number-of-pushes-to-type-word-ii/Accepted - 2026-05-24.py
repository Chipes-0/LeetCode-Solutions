class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        N = len(c)
        out, val, count = 0, 1, 0
        c = sorted(c.items(), key=lambda x:x[1], reverse=True)
        for v in c:
            count += 1
            if count == 9:
                val += 1
                count = 0
            out += val * v[1]
        return out