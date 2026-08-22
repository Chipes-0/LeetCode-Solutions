class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        out = 0
        halfs = [x//2 for x in nums[1:]]
        left = 0
        right = 2
        n = len(nums)
        while right < n:
            acum = nums[left] + nums[right]
            if acum == halfs[left]:
                out += 1
            left += 1
            right += 1
        return out
            