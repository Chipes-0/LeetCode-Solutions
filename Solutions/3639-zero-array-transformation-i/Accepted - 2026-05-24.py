class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        psum = [0] * n
        for q in queries:
            l, r = q
            for i in range(l, r+1):
                psum[i] += 1

        for i in range(n):
            if nums[i] - psum[i] > 0:
                return False
        return True