class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        out = 0
        count = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                count += 1
            else:
                count += 1
                k -= 1
                while k == -1:
                    if nums[left] == 0:
                        k += 1
                    count -= 1
                    left += 1
            if count > out:
                out = count 
        return out