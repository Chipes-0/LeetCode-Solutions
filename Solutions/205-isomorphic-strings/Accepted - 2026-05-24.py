class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        maping = {}
        for i in range(len(s)):
            if s[i] not in maping:
                maping[s[i]] = t[i]
            if t[i] != maping[s[i]]:
                return False
        return True