class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = 0
        total = 0
        last = ""

        for ch in s:
            if ch == "(":
                stack += 1
            else:
                stack -= 1
            
            if last == "(" and ch == ")":
                total += 2 ** stack
            last = ch
        
        return total
