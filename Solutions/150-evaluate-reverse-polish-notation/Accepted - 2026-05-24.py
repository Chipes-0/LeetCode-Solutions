class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ['+', '-', '*', '/']
        for element in tokens:
            if element not in operations:
                stack.append(int(element))
            elif element == '+':
                n = stack.pop() + stack.pop()
                stack.append(n)
            elif element == '-':
                n = stack.pop() - stack.pop()
                stack.append(n)
            elif element == '*':
                n = stack.pop() * stack.pop()
                stack.append(n)
            else:
                a, b = stack.pop(), stack.pop()
                n = b / a
                stack.append(int(n))
        return stack[0]