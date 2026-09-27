class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def grammar(s):
            parts = set()
            curr = {""}
            i = 0
            while i < len(s):
                if s[i] == "{":
                    j = i
                    depth = 0
                    while True:
                        if s[j] == "{":
                            depth -= 1
                        elif s[j] == "}":
                            depth += 1
                        
                        if depth == 0:
                            break
                        j += 1
                        
                    
                    options = grammar(s[i + 1: j])
                    temp = set()
                    for op in options:
                        for cu in curr:
                            temp.add(cu + op)
                    curr = temp
                    i = j + 1

                elif s[i] == ",":
                    parts |= curr
                    curr = {""}
                    i += 1
                else:
                    temp = set()
                    for x in curr:
                        temp.add(x + s[i])
                    curr = temp
                    i += 1

            parts |= curr
            return parts
        
        return sorted(list(grammar(expression)))