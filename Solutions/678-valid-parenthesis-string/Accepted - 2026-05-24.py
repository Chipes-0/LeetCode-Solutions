class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        count = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append("(")
            if s[i] == ")":
                if stack:
                    stack.pop()
                elif count:
                    count -= 1
                else:
                    return False
            else:
                count += 1
        if count >= len(stack):
            return True
        return False