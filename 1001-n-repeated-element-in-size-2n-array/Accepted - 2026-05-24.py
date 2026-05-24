class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        reps = len(nums) // 2
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
            if freq[n] == reps:
                return n
        return 0