class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        out = ""
        balance = 0
        for i, ch in enumerate(s):
            if ch == "(":
                balance += 1
                if balance == 1:
                    continue
            else:
                balance -= 1
                if balance == 0:
                    continue
            out += ch
        
        return out            

