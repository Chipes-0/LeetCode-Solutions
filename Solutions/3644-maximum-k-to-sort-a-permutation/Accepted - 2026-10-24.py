from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        out = None
        for index, num in enumerate(nums):
            if index == num:
                continue
            if out == None:
                out = num
            out = out & num
        if out == None:
            return 0
        return out