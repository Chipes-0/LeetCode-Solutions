from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        curr = k
        while True:
            if curr not in s:
                return curr
            curr += k
        return 0