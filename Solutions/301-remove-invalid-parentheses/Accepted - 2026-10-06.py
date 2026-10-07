class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        out = set()
        N = len(s)
        minDel = N
        def bt(index, deleted, string, balance):
            nonlocal out, minDel
            if deleted > minDel:
                return

            if index == N:
                if balance == 0:
                    if deleted < minDel:
                        minDel = deleted
                        out = {string}
                    elif deleted == minDel:
                        out.add(string)
                return
            
            if s[index] == "(":
                ## Keep
                bt(index + 1, deleted, string + '(', balance + 1)
                ## Remove
                bt(index + 1, deleted + 1, string, balance)
            elif s[index] == ")":
                ## Keep
                if balance > 0:
                    bt(index + 1, deleted, string + ')', balance - 1)
                ## Remove    
                bt(index + 1, deleted + 1, string, balance)
            else:
                bt(index + 1, deleted, string + s[index], balance)
        
        bt(0, 0, "", 0)
        return list(out)
