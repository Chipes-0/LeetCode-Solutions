from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        N = len(nums)
        out = 0

        for i in range(N):
            for j in range(i, N):
                unique = set(nums[i : j + 1])
                out += len(unique) ** 2
        return out