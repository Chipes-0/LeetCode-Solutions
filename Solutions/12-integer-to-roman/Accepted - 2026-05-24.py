def helper(num: int) -> str:
    strnum = str(num)
    values = []
    roman = ""
    if num == 0:
        return ""
    x = num // pow(10, len(str(num)) - 1)
    if len(strnum) < 2:
        values = ["I", "V", "X"]
    elif len(strnum) < 3:
        values = ["X", "L", "C"]
    elif len(strnum) < 4:
        values = ["C", "D", "M"]
    else:
        values = ["M", "", ""]

    if x in [0, 1, 2, 3]:
        roman = values[0] * int(x)
    elif x == 4:
        roman = values[0] + values[1]
    elif x == 5:
        roman = values[1]
    elif x in [6, 7, 8]:
        roman = values[1]
        roman += values[0] * int(x % 5)
    else:
        roman = values[0] + values[2] 
    return roman + helper(num - x * pow(10, len(str(num)) - 1))

class Solution:
    def intToRoman(self, num: int) -> str:
        return helper(num)