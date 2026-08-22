class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefixsum = 0
        total = sum(nums)
        out = 0
        for n in nums:
            prefixsum += n
            if prefixsum >= (total - prefixsum):
                print(prefixsum)
                out += 1
        return out - 1