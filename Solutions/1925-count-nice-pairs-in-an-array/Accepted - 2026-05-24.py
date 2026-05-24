class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        rev = [int(str(x)[::-1]) for x in nums]
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + rev[j] == nums[j] + rev[i]:
                    count += 1
                    print(nums[i], rev[j])
                    print(nums[j], rev[i])
        return count