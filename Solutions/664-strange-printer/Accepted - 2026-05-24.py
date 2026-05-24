class Solution:
    def strangePrinter(self, s: str) -> int:
        sout = s[0] * len(s)
        n = 1
        for i in range(len(s)):
            if sout[i] != s[i]:
                end = s.rfind(s[i])
                n += 1
                temp = list(sout)
                for j in range(i, end + 1):
                    temp[j] = s[i]
                sout = "".join(temp)
        print(sout)
        return n