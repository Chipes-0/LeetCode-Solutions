class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        out = 0
        left = 0
        for right in range(len(nums)):
            product *= nums[right]                
            while product >= k and left <= right:
                product /= nums[left]
                left += 1
            out += right - left + 1
        return out