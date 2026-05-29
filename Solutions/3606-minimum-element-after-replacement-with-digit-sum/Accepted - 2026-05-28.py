class Solution:
    def minElement(self, nums: List[int]) -> int:
        out = float("inf")
        for num in nums:
            suma = 0
            while num != 0:
                suma += num % 10
                num //= 10
            out = min(out, suma)
        return out