class Solution:
    def longestBalanced(self, s: str) -> int:
        out = 0
        for i in range(len(s)):
            d = defaultdict(int)
            for j in range(i, len(s)):
                update = True
                d[s[j]] += 1
                same = d[s[j]]
                for key in d:
                    if d[key] != same:
                        update = False
                        break
                if update:
                    out = max(out, j - i + 1)

        return out