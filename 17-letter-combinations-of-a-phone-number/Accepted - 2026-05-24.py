class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtraking(s: List[str], index: int) -> None:
            nonlocal res, n
            if len(s) == n:
                res.append("".join(s))
                return
            for l in letters[digits[index]]:
                s.append(l)
                backtraking(s, index + 1)
                s.pop()
                
        if digits == "":
            return []
        res, n = [], len(digits)
        backtraking([], 0)
        return res