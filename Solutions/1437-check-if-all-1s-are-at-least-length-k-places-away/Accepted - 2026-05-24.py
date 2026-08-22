class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                for j in range(1, k + 1):
                    if i + j >= len(nums):
                        break
                    if nums[i + j] == 1:
                        return False
                i += k 
            else:
                i += 1
        return True