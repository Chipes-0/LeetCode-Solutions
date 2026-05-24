class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1, s2 = "", ""
        for l in s:
            if l != "#":
                s1 += l
            else:
                s1 = s1[:-1]
        
        for l in t:
            if l != "#":
                s2 += l
            else:
                s2 = s2[:-1]
        return s1 == s2