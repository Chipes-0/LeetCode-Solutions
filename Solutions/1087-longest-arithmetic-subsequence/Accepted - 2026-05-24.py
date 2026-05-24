from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                n = nums[j] - nums[i]
                if not d[n]:
                    d[n] = 1
                else:
                    d[n] += 1
        return max(d.values()) + 1
