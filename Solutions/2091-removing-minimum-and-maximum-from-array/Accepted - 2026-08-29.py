from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        vmin = float("inf")
        vmax = float("-inf")
        imin = -1
        imax = -1

        for index, num in enumerate(nums):
            if num > vmax:
                vmax = num
                imax = index
            if num < vmin:
                vmin = num
                imin = index

        n = len(nums)
        imin, imax = imin + 1, imax + 1
        left = max(imax, imin)
        right = n - min(imax, imin) + 1
        both = min(imax, imin) + (n - max(imax, imin) + 1)

        return min(left, right, both)