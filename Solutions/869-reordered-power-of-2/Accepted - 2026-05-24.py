class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = set()
        p = 0 
        dos = 2
        while dos ** p < 10000000000:
            s.add(''.join(sorted(str(dos ** p))))
            p += 1
        
        return ''.join(sorted(str(n))) in s