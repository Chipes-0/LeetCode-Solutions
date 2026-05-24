class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        suma = 0
        def arrayXOR(nums: List[int]) -> int:
            res = 0
            for num in nums:
                res ^= num
            return res
            
        def backtrack(i, subset):
            nonlocal suma
            if i == len(nums):
                suma += arrayXOR(subset)
                return
            backtrack(i + 1, subset.copy())
            subset.append(nums[i])
            backtrack(i + 1, subset.copy())
        backtrack(0, [])

        return suma
