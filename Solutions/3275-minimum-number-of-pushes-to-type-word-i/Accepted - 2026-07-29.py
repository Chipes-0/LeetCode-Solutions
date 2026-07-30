class Solution:
    def minimumPushes(self, word: str) -> int:
        arr = [0] * 26
        for ch in word:
            arr[ord(ch) - ord('a')] += 1
        arr.sort(reverse = True)
        out = 0
        for i in range(26):
            out += arr[i] * ((i // 8) + 1)
        return out
