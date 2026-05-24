class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        out = 0 
        for word in words:
            flag = True
            for w in word:
                if w not in allowed:
                    flag = False
                    break
                    
            if flag:
                out += 1
        return out