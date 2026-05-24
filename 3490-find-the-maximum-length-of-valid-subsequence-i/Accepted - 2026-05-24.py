class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums = list(map(lambda x: x & 1, nums))
        