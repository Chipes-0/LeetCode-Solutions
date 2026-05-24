class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        h = dict()
        big = 0
        for n in nums:
            if -n in h:
                big = max(abs(n), big)
            h[n] = 1
        return big if big > 0 else -1