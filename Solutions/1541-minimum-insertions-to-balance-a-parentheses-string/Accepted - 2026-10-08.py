class Solution:
    def minInsertions(self, s: str) -> int:
        stack = 0
        out = 0

        for ch in s:
            if ch == "(":
                stack += 2
                if stack % 2 == 1:
                    out += 1
                    stack -= 1
            else:
                stack -= 1
                if stack < 0:
                    out += 1
                    stack = 1
        
        return out + stack