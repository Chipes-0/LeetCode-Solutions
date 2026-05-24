class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 0
        i = 0
        l = ""
        N = len(chars)
        while N:
            if chars[0] != l:
                chars.append(l)
                if count > 1:
                    for c in str(count):
                        chars.append(c)
                l = chars.pop(0)
                count = 1
            else:
                chars.pop(0)
                count += 1
            N -= 1
        chars.append(l)
        if count > 1:
            for c in str(count):
                chars.append(c)
        chars.pop(0)
        return len(chars)