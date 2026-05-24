class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strArr = []
        rango = range(numRows)
        up = rango[numRows - 1]
        index = 0
        topdown = False
        for i in range(numRows):
            strArr.append("")
        
        for i in range(len(s)):
            if index % numRows in [0, up]:
                topdown = not topdown

            strArr[index] += s[i]
            if topdown:
                index += 1
            else:
                index -= 1
        for i in range(1, numRows):
            strArr[0] += strArr[i]
        return strArr[0]

