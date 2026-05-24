class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hm = [0] * 10**5
        for n in nums:
            if n > 0:
                hm[n] = 1
        
        for i in range(1, 10**5):
            if not hm[i]:
                return i 
        return 10**5 + 1