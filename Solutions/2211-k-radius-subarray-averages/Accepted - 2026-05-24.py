from statistics import mean

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums): return [-1 for i in range(len(nums))]
        out = [-1 for i in range(k * 2)]
        for i in range(len(nums) - 2 * k):
            out.insert(i + k, int(mean(nums[i: i + 2 * k + 1])))
        return out

        