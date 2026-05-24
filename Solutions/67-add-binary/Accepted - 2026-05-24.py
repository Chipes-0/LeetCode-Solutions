class Solution:
    def addBinary(self, a: str, b: str) -> str:
        size = max(len(a), len(b))
        res = ["0"] * (size + 1)
        a = a.zfill(size)[::-1]
        b = b.zfill(size)[::-1]

        carry = 0

        for i in range(size):
            if a[i] != b[i]:
                if carry:
                    res[i] = "0"
                    carry = 1
                else:
                    res[i] = "1"
                    carry = 0
            else:
                one = a[i] == "1"
                if not one:
                    if carry:
                        res[i] = "1"
                    else:
                        res[i] = "0"
                    carry = 0
                else:
                    if carry:
                        res[i] = "1"
                    else:
                        res[i] = "0"
                    carry = 1
        if carry:
            res[-1] = "1"
        return "".join(res[::-1])
