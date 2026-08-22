class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        equal = sum(nums)//len(nums)
        nums = list(map(lambda x : abs(x - equal), nums))
        out = 0
        nums = sorted(nums)[::-1]
        cost = sorted(cost)
        
        for i, n in enumerate(nums):
            out += n * cost[i]
        return out
