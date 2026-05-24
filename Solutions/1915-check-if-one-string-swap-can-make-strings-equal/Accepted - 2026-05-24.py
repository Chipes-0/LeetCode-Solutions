class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1_mis = ""
        s2_mis = ""
        if len(s1) != len(s2):
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                s1_mis += s1[i]
                s2_mis += s2[i]
        if len(s1_mis) != 0 and len(s1_mis) != 2:
            return False
        return sorted(s1_mis) == sorted(s2_mis)
        
        