class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        nums2 = [nums[0]]
        for num in nums:
            if num != nums2[-1]:
                nums2.append(num)
        out = 0
        
        for i in range(1, len(nums2) - 1):
            if nums2[i-1] < nums2[i] > nums2[i + 1] or nums2[i-1] > nums2[i] < nums2[i + 1]:
                out += 1
        return out