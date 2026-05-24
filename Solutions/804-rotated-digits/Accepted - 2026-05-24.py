class Solution:
    def rotatedDigits(self, n: int) -> int:
        nstr = str(n)  
        digits = len(nstr)
        out = 0
        # previous digits
        for i in range(digits - 1):
            out += pow(4, i + 1)
        # curr digit
        
        def numgen(num):
            possible = ["2","5","6","9"]
            nonlocal digits, out, n
            if len(num) == digits:
                if int(num) <= n:
                    out += 1 
                return
            for d in possible:
                numgen(num + d)
        numgen("")
        return out
