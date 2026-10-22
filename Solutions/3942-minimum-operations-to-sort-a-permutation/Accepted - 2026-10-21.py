from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        
        if N < 3:
            if nums[-1] == N - 1:
                return 0
            return 1
        
        def valid(d):
            flag = True
            for i in range(N):
                if (nums[(i + 1) % N]) != ((nums[i] + d) % N):
                    flag = False
                    break
            return flag
        
        ans = float("inf")
        ## Rotacion ordenada
        if valid(1):
            if nums[0] == 0:
                ans = 0
            else:
                ans = min(N - nums[0], nums[0] + 2)
        ## Rotacion inversa
        elif valid(-1):
            ans = min(ans, (nums[0] + 1) % N + 1, (N - 1 - nums[0]) % N + 1)
        
        if ans == float("inf"):
            return -1
        return ans

