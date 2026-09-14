from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0] < rec2[0]:
            first = rec1
            second = rec2
        else:
            first = rec2
            second = rec1

        if first[2] <= second[0]:
            return False
        
        if rec1[1] < rec2[1]:
            first = rec1
            second = rec2
        else:
            first = rec2
            second = rec1

        if first[3] < second[1]:
            return False
        return True