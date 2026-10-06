class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        out = 0
        for ch in s:
            if ch == "(":
                if balance < 0:
                    balance = 0
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                out += 1
                
        if balance > 0:
            out += balance
        return out