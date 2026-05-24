class Solution:
    def reverse(self, x: int) -> int:
        str1 = str(x)
        if str1[0] in ["-", "+"]:
            str1 = str1[0] + str1[1:][::-1]
        else:
            str1 = str1[::-1]
        return int(str1)