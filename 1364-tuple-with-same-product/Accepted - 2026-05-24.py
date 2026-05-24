class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        out = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                freq[nums[i] * nums[j]] += 1
        for n in freq.values():
            if n >= 2:
                out += 8 * ((n * n) - n) // 2
        return out