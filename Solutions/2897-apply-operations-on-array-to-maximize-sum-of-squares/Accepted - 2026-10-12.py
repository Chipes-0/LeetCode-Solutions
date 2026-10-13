from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MODULO = 10**9 + 7
        N = max(nums).bit_length()
        
        arr = [0] * N
        for i in range(N):
            for num in nums:
                if num & (1 << i):
                    arr[i] += 1
                
        out = 0
        for _ in range(k):
            num = 0
            for i in range(N):
                if arr[i]:
                    num += 2 ** i
                    arr[i] -= 1
            out += (num * num) % MODULO
        
        return out % MODULO