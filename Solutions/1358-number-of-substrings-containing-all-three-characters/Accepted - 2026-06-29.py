class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        left = 0
        out = 0
        count = {'a': 0, 'b': 0, 'c': 0}
        for right in range(N):
            count[s[right]] += 1
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                out += (N - right)
                count[s[left]] -= 1
                left += 1
        return out