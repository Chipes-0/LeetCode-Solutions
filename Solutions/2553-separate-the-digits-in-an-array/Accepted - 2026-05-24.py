class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        def separate(num):
            return [int(x) for x in list(str(num))]

        out = []
        for num in nums:
            out += separate(num)
        return out