from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            total = 0
            while num:
                total += num % 10
                num //= 10
            if i == total:
                return i
        return -1