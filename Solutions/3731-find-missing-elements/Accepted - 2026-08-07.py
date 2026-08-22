from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        minN,maxN = float("inf"), 0
        arr = [0] * 101
        for num in nums:
            minN = min(minN, num)
            maxN = max(maxN, num)
            arr[num] = 1
        
        out = []
        for i in range(minN, maxN):
            if not arr[i]:
                out.append(i)
        return out