class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out = [max(nums[0:k])]
        for i in range(k, len(nums)):
            
            if nums[i] > out[-1]:
                out.append(nums[i])
            else:
                out.append(out[-1])
        return out
