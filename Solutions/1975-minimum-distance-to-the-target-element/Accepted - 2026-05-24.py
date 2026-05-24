class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        out = float("inf")
        for i in range(len(nums)):
            if nums[i] == target:
                out = min(out, abs(i - start))
        return out