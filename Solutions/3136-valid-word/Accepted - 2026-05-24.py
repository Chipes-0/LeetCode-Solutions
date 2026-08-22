class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        c, v = 0, 0
        for w in word:
            if w in "aeiou":
                v += 1
            elif w.isalpha():
                c += 1
            elif w.isdigit():
                continue
            else:
                return False
        return not not (c and v)