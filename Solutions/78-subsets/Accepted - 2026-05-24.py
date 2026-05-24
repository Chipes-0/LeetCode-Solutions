class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtracking(array: List[int], start: int) -> None:
            nonlocal res, nums
            res.append(array[:])
            for i in range(start, len(nums)):
                array.append(nums[i])
                backtracking(array, i + 1)
                array.pop()
        res = []
        backtracking([], 0)
        return res