class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        out = 0
        power = 0
        for char in columnTitle[::-1]:
            val = ord(char) - ord("A") + 1
            out += (26 ** power) * val
            power += 1
        return out