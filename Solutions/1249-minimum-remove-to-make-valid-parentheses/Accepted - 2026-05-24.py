class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        out = ""
        count1 = count2 = 0
        for i in range(len(s)):
            if s[i] == "(":
                count1  += 1
            if s[i] == ")":
                count2 += 1
            if count1 >= count2:
                out += s[i]
            else:
                count2 -= 1
        s = out
        out = ""
        N = len(s) - 1
        for i in range(len(s)):
            if s[N - i] == "(":
                count1  += 1
            if s[ N - i] == ")":
                count2 += 1
            if count2 >= count1:
                out = s[N - i] + out
            else:
                count2 -= 1
        return out