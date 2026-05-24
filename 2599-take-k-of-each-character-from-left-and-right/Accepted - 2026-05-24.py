class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count = Counter(s)
        N = len(s)
        out = 0
        start = 0
        if count['a'] < k or count['b'] < k or count['c'] < k:
            return -1
        for end in range(N):
            count[s[end]] -= 1
            if count['a'] >= k and count['b'] >= k and count['c'] >= k:
                out = max(out, end - start + 1)
            else:
                count[s[start]] += 1
                start += 1
        return N - out