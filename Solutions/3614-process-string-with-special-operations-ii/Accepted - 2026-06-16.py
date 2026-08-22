class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0
        for ch in s:
            if ch in "*%#":
                if ch == "*" and length > 0:
                    length -= 1
                elif ch == "#":
                    length *= 2
                else:
                    pass
            else:
                length += 1
                
        if k >= length:
            return "."
        actual_length = length
        for ch in s[::-1]:
            if ch in "#%*":
                if ch == "#":
                    half = actual_length // 2
                    if k >= half:
                        k -= half
                    actual_length = half
                elif ch == "%":
                    k = actual_length - 1 - k
                else:
                    actual_length += 1
            else:
                actual_length -= 1
                if k == actual_length:
                    return ch
        return "."