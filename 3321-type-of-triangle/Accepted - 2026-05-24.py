class Solution:
    def triangleType(self, nums: List[int]) -> str:
        sides = set(nums)
        if (nums[0] + nums[1]) > nums[2] and (nums[0] + nums[2]) > nums[1] and (nums[2] + nums[1]) > nums[0]:
            pass
        else:
            return "none"
        if len(sides) == 1:
            return "equilateral"
        elif len(sides) == 2:
            return "isosceles"
        else:
            return "scalene"
        