class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        out = window / k
        for i in range(k, len(nums)):
            window += nums[i] - nums[i - k]
            avg = window / k
            if avg > out:
                out = avg
        return out
            
        