class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word = "".join(set(word))
        h = dict()
        out = 0
        for c in word:
            if c in h:
                out += 1
            else:
                if c >= 'a' and c <= 'z':
                    h[c.upper()] = True
                else:
                    h[c.lower()] = True
        return out