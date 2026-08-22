class Solution:
    def check(self, nums: List[int]) -> bool:
        lifes = 2
        for i in range(len(nums)):
            if nums[i-1] > nums[i]:
                lifes -= 1
                if not lifes:
                    return False
        return True