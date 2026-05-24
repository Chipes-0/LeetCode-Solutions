class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        values = []

        def bt(s):
            nonlocal values
            if len(s) > 1 and s[-1] == s[-2]:
                return
            if len(s) == n:
                values.append(s)
                return 
            for ch in "abc":
                bt(s + ch)
        
        bt("")
        values.sort()
        if k > len(values):
            return ""
        return values[k - 1]