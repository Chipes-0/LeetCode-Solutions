class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        out = 0
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1
            if count > out:
                out = count
        return out