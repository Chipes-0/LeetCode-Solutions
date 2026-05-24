class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MODULO = 10**9 + 7
        while queries:
            l, r, k, v = queries.pop(0)
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % MODULO
        
        out = 0
        for n in nums:
            out ^= n
        return out