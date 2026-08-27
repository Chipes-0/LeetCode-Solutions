from collections import defaultdict

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = defaultdict(int)
        n = len(s)
        for ch in s:
            count[ch] += 1

        def bt(index, curr, greater):
            if index == n:
                return curr if greater else ""
            start = 0 if greater else ord(target[index]) - ord('a')
            for char in range(start, 26):
                char = chr(ord('a') + char)
                if count[char]:
                    count[char] -= 1
                    out = bt(index + 1, curr + char, greater or char > target[index])
                    count[char] += 1

                    if out:
                        return out
            return ""
        return bt(0, "", False)