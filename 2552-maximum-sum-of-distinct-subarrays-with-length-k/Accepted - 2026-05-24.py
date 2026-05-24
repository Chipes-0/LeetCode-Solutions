class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        m = dict()
        out, current = 0, 0
        for i in range(k):
            if nums[i] in m:
                current = 0
                m = dict()
                break
            m[nums[i]] = True
            current += nums[i]
        out = current 
        if k > len(nums):
            return out
        for i in range(1, len(nums) - k):
            del m[nums[i - 1]]
            current -= nums[i - 1]
            current += nums[i + k - 1]
            if nums[i + k - 1] not in m:
                out = max(out, current)
            m[nums[i + k - 1]] = True
        return out