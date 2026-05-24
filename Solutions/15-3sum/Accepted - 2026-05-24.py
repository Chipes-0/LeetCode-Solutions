class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        N = len(nums)
        out = []
        nums.sort()
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = N - 1

            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                if curr > 0:
                    right -= 1
                elif curr < 0:
                    left += 1
                else:
                    out.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return out