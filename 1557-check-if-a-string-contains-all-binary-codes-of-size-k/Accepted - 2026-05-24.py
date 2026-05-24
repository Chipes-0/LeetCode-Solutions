class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        existing = {}
        if k > len(s):
            return False
        for i in range(len(s) - k):
            if s[i: i + k] in existing:
                continue
            existing[s[i: i + k]] = True
        return len(existing) == 2 ** k