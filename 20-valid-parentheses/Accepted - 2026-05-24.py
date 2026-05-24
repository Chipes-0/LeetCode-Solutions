class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        for i in list(s):
            if i in ["(", "[", "{"]:
                queue.append(i)
            else:
                char = queue.pop(len(queue) - 1)
                if char == "{" and i != "}": 
                    return False
                elif char == "[" and i != "]": 
                    return False
                elif char == "(" and i != ")": 
                    return False
        if queue == []:
            return True