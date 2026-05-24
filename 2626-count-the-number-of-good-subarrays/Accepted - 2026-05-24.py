class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        count = 0
        out = 0
        l = 0
        for r in range(len(nums)):
            count += freq[nums[r]]
            freq[nums[r]] += 1

            while count >= k:
                freq[nums[l]] -= 1
                count -= freq[nums[l]] 
                l += 1
            out += l
        return out
            