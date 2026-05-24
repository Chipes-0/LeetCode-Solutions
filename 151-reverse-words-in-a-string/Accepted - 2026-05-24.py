class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        out = ""
        print(s)
        for i in range(len(s) - 1, -1, -1):
            if s[i] != '':
                out += s[i] + " "
        return out[:-1]