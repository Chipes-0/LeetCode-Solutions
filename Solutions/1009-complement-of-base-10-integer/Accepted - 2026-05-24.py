class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        num = ""
        while n:
            if n & 1:
                num += "0"
            else:
                num += "1"
            
            n //= 2
        return int(num[::-1], 2)