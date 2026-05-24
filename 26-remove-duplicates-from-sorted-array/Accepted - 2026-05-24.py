class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        seen = set()
        for n in nums:
            if n in seen:
                continue
            nums[i] = n
            i += 1
            seen.add(n)
        return i