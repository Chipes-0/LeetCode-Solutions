class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        out = ""
        while columnNumber:
            columnNumber -= 1
            out = chr(ord("A") + columnNumber % 26) + out
            columnNumber //= 26
        return out