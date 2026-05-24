class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        options = {}
        res = []
        for i, n in enumerate(nums):
            diff = target - n
            if diff in options:
                return [i, options[diff]]
            else:
                options[n] = i
