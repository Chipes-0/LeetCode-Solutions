from collections import Counter

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def noPermutations(counter1: dict) -> bool:
            nonlocal res
            for arr in res:
                counter2 = Counter(arr)
                if counter1 == counter2:
                    return False
            return True

        def backtracking(array: List[int]) -> None:
            nonlocal res
            s = sum(array)
            if s == target:
                if noPermutations(Counter(array)):
                    res.append(array[:])
            for i in range(len(candidates)):
                array.append(candidates[i])
                if sum(array) <= target:
                    backtracking(array)
                array.pop()
        res = []
        backtracking([])
        return res