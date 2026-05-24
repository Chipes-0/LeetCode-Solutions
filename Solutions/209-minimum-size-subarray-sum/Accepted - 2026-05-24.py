class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = float('inf')
        suma = index = l = 0
        if sum(nums) < target: 
            return suma
        for i in range(len(nums)):
            l += 1
            suma += nums[i]
            while suma >= target:
                minlen = min(minlen, l)
                suma -= nums[index]
                l -= 1
                index += 1

        return minlen

            