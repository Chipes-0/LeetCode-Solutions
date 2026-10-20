class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        out = []

        for index, num in enumerate(nums):
            if num == target:
                out.append(index)
        return out