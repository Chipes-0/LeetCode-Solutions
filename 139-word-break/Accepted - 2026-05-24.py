class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def backtracking(index: int) -> None:
            nonlocal flag
            if index == len(s):
                flag = True
                return 
            for word in wordDict:
                n = len(word)
                if s[index : index + n] == word:
                    backtracking(index + n)
        flag = False   
        backtracking(0)
        return flag
        