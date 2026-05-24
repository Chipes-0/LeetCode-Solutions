class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count = 0
        s = s.lower()
        half = len(s) // 2
        for i in range(half):
            if s[i] in "aeiou":
                count += 1
            if s[half + i] in "aeiou":
                count -= 1
        return count == 0