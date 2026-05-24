class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(comb: List[int], curr: int) -> None:
            nonlocal res
            if len(comb) == k:
                res.append(comb[:])
                return
            for i in range(curr, n + 1):
                comb.append(i)
                backtracking(comb, i + 1)
                comb.pop()
        res = []
        backtracking([], 1)
        return res