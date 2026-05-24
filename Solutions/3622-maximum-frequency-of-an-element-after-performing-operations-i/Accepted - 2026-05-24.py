class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        l = 0
        out = 0
        numOps = numOperations
        for r in range(len(nums)):
            if nums[l] == nums[r]:
                pass
            elif nums[l] + k >= nums[r] and numOps:
                numOps -= 1
            else:
                l += 1
            out = max(out, r-l+1)
        return out
