from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        n = len(nums)
        for i in range(min(k + 1, n)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        
        for i in range(k + 1, n):
            seen.remove(nums[i - k - 1])
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False
             