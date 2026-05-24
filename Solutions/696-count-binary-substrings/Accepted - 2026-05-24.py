class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        arr = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                arr.append(count)
                count = 1
        arr.append(count)
        out = 0
        for i in range(1, len(arr)):
            out += min(arr[i], arr[i - 1])
        return out