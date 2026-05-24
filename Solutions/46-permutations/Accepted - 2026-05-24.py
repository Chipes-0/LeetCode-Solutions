class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(array: List[int], possible: List[int]) -> None:
            nonlocal res
            if not possible:
                res.append(array[:])
                return 
            for n in possible:
                pop = possible.pop(0)
                array.append(pop)
                backtracking(array, possible[:])
                array.pop()
                possible.append(pop)
                
        res = []
        backtracking([], nums)
        return res
