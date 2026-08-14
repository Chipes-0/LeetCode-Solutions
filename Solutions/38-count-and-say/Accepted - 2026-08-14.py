class Solution:
    def countAndSay(self, n: int) -> str:
        def RLE(num):
            out = ""
            count = 1
            val = num[0]
            for ch in num[1:]:
                if ch == val:
                    count += 1
                else:
                    out += str(count) + val
                    val = ch
                    count = 1
            out += str(count) + val
            return out

        def recCountAndSay(n):
            if n == 1:
                return "1"
            return RLE(recCountAndSay(n - 1))
        
        return recCountAndSay(n)