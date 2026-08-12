from typing import List
from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        out = 0
        left = 0
        for right in range(len(nums)):
            count[nums[right]] += 1
            while left < right and count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1
            out = max(out, right - left + 1)
        return out