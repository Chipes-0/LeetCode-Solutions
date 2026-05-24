class Solution:
    def findComplement(self, num: int) -> int:
        binary = reversed(bin(num)[2:])
        complement = ""
        for bit in binary:
            if bit == '0':
                complement += "1"
            else:
                complement += "0"
        return int(complement, 2)