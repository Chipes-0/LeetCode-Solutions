class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # abcdba     acb     
        # cabdab     cba

        even1 = []
        odd1 = []
        even2 = []
        odd2 = []

        for i in range(len(s1)):
            if i & 1:
                odd1.append(s1[i])
                odd2.append(s2[i])
            else:
                even1.append(s1[i])
                even2.append(s2[i])
        
        even1.sort()
        odd1.sort()
        even2.sort()
        odd2.sort()

        return "".join(even1) == "".join(even2) and "".join(odd1) == "".join(odd2)