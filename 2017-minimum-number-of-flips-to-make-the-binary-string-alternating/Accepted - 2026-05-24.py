class Solution:
    def minFlips(self, s: str) -> int:
        oddz, oddo = 0, 0
        evenz, eveno = 0, 0
        N = len(s)

        for i in range(N):
            if i & 1:
                if s[i] == "0":
                    oddz += 1
                else:
                    oddo += 1
            else:
                if s[i] == "0":
                    evenz += 1
                else:
                    eveno += 1
        if N % 2 == 0:
            return min(oddz + eveno, oddo + evenz)
        
        out = float("inf")
        for i in range(N):
            if i & 1:
                if s[i] == "0":
                    oddz -= 1
                    evenz += 1
                else:
                    oddo -= 1
                    eveno += 1
            else:
                if s[i] == "0":
                    evenz -= 1
                    oddz += 1
                else:
                    eveno -= 1
                    oddo += 1
            out = min(out, oddz + eveno, oddo + evenz)
        return out
            
            