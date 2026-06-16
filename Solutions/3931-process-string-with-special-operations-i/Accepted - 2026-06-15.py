from collections import deque

class Solution:
    def processStr(self, s: str) -> str:
        stack = deque()
        direction = 1
        popfunc = stack.pop if direction else stack.popleft
        appendfunc = stack.append if direction else stack.appendleft
        extendfunct = stack.extend
        for ch in s:
            if ch == "*" and stack:
                popfunc()
            elif ch == "#" and stack:
                extendfunct(stack)
            elif ch == "%" and stack:
                direction = (direction + 1) & 1
                popfunc = stack.pop if direction else stack.popleft
                appendfunc = stack.append if direction else stack.appendleft
            elif ch not in "*%#":
                appendfunc(ch)
        return "".join(stack) if direction else "".join(reversed(stack))