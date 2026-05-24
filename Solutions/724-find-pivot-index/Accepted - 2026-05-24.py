class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum_1 = [0]
        
        for num in nums:
            prefix_sum.append(num + prefix_sum[-1])
        print(prefix_sum)
        return -1