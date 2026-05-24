class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        out = []
        for n in nums:
            f = True
            for i in range(1, n):
                if i | i + 1 == n:
                    out.append(i)
                    f = False
                    break
            if f:
                out.append(-1)
        return out