from typing import List

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        arr = [0, 0, 0]
        for num in stones:
            arr[num % 3] += 1
        
        if arr[0] % 2 == 0:
            return arr[1] > 0 and arr[2] > 0
        
        return abs(arr[1] - arr[2]) > 2