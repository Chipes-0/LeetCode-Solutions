class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        words = [(int(x[-1]), x[:-1]) for x in words]
        words.sort()

        out = ""
        for word in words:
            out += word[1] + " "
        return out[:-1]