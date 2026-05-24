class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        no_duplicates = set(nums)
        return len(no_duplicates) != len(nums)