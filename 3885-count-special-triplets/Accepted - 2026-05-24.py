import math

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        out = 0
        for n in nums:
            if n in counts and n//2 in counts and n % 2 == 0 and n != 0:
                out += counts[n//2]
            counts[n] += 1
        zeros = nums.count(0)
        if zeros > 2:
            out += math.comb(zeros, 3)
        return out
