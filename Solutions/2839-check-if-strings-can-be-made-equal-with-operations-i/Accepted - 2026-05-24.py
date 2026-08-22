class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        options = []
        options.append(s1)
        s1 = list(s1)
        s1[0], s1[2] = s1[2], s1[0]
        options.append("".join(s1))

        s1[1], s1[3] = s1[3], s1[1]
        options.append("".join(s1))

        s1[0], s1[2] = s1[2], s1[0]
        options.append("".join(s1))

        if s2 in options:
            return True
        
        return False