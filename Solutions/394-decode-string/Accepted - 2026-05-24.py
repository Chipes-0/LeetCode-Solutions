class Solution:
    def decodeString(self, s: str) -> str:
        stack_nums = []
        stack_chars = []
        out = ""
        num = ""
        for c in s:
            if c >= '0' and c <='9':
                num += c
            elif c == "[":
                stack_nums.append(int(num))
                num = ""
                stack_chars.append(c)
            elif c == "]":
                string = ""
                while stack_chars and stack_chars[-1] != "[":
                    string += stack_chars[-1]
                    stack_chars.pop()
                string = string[::-1]
                if stack_chars:
                    stack_chars.pop()
                stack_chars.append(string * stack_nums[-1])
                stack_nums.pop()
            else:
                stack_chars.append(c)
        for e in stack_chars:
            out += e
        return out