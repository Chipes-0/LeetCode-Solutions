class Solution:
    def compressedString(self, word: str) -> str:
        out = ""
        count = 1
        for i in range(len(word) - 1):
            if word[i] != word[i + 1]:
                out += str(count) + word[i]
                count = 1
            elif count == 9:
                out += "9" + word[i]
                count = 1
            else:
                count += 1
        if len(word) >= 2 and word[-1] == word[-2]:
            if count + 1 <= 9:
                out += str(count) + word[-1]
        else:
            out += "1" + word[-1]
        return out
