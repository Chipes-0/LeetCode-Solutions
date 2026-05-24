class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        out = 0
        for _ in range(2):
            stack = [] 
            if x > y:
                w = "ab"
                add = x
            else:
                w = "ba"
                add = y
            for l in s:
                if stack and stack[-1] == w[0] and l == w[1]:
                    stack.pop()
                    out += add
                else:
                    stack.append(l)
            if x == add:
                x = 0
            else:
                y = 0
            s = ''.join(stack)
        return out