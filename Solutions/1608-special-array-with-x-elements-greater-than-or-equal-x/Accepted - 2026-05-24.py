class Solution:
    def specialArray(self, nums: List[int]) -> int:
        def count_array(x):
            count = 0
            for n in nums:
                if n >= x:
                    count += 1
            return count
        
        for i in range(len(nums) + 1):
            x = count_array(i)
            if i == x:
                return i
        return -1

