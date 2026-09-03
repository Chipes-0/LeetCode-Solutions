from typing import list

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        smallodd = float("inf")
        smalleven = float("inf")
        N = len(nums1)
        for i in range(N):
            if not nums1[i] & 1:
                smalleven = min(smalleven, nums1[i])
            else:
                smallodd = min(smallodd, nums1[i])
        
        if smallodd  == float("inf") or smalleven == float("inf"):
            return True
        
        return smalleven > smallodd
