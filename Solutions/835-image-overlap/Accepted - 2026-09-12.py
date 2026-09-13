from typing import List
from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        count = defaultdict(int)
        N = len(img1)
        coord1 = []
        coord2 = []

        for i in range(N):
            for j in range(N):
                if img1[i][j] == 1:
                    coord1.append((i, j))
                
                if img2[i][j] == 1:
                    coord2.append((i, j))
        
        for A1 in coord1:
            for A2 in coord2:
                dr, dc = A1[0] - A2[0], A1[1] - A2[1]

                count[(dr, dc)] += 1
        if not count.values():
            return 0
        return max(count.values())