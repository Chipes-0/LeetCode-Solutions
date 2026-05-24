class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        out = 0
        for n in nums:
            out += (len(str(n)) + 1) % 2
        return out