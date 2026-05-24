class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        N = len(s)
        memo = [0] * 26
        for i in range(N):
            current = ord(s[i]) - ord('a')
            longest = 1
            for prev in range(26):
                if abs(current - prev) <= k:
                    print(prev)
                    longest = max(longest, memo[prev] + 1)
            memo[current] = max(memo[current], longest)
        return max(memo)
        