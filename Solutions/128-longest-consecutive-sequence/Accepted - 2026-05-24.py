class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        count = 0
        maxcount = 0
        for i in range(1, len(nums)):
            count += 1
            if nums[i] != nums[i - 1] + 1:
                if count > maxcount:
                    maxcount = count
                count = 1
        if count > maxcount:
            maxcount = count
        return maxcount