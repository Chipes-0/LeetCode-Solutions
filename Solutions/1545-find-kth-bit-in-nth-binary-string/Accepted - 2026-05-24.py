class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert_binary(s: str) -> str:
            n = int(s, 2)
            mask = (1 << len(s)) - 1
            return format(n ^ mask, f'0{len(s)}b')
        s1 = "0"
        while len(s1) <= k:
            s1 = s1 + "1" + invert_binary(s1)[::-1]
        return s1[k - 1]