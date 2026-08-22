class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        inc = 0
        for i in range(1, len(nums)):
            if inc & 0:
                if nums[i] < nums[i - 1]:
                    inc += 1
            else:
                if nums[i] > nums[i - 1]:
                    inc += 1
        print(inc)
        return inc == 3
