from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        c = Counter(s)
        out = ""
        op = ""
        for i in range(26):
            ch = chr(ord('a') + i)
            rep = c[ch] // 2
            out += ch * rep
            c[ch] -= rep * 2
            if c[ch] and not op:
                op = ch
        
        return out + op + "".join(reversed(out))