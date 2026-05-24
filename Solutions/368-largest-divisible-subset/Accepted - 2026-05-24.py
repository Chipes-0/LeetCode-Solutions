class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        longest = [[] for _ in range(len(nums))]
        for i in range(len(nums)):
            longest[i] += [nums[i]]
            for j in range(i):
                print(nums[i], nums[i - j - 1])
                if nums[i] % nums[i - j - 1] == 0 and len(longest[i]) < len(longest[i - j - 1]) + 1:
                    longest[i] += longest[i - j - 1]
        return max(longest, key=lambda x: len(x))