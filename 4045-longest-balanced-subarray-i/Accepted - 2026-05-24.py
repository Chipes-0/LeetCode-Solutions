class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        odd = dict()
        even = dict()

        out = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] & 1:
                    if nums[j] not in odd:
                        odd[nums[j]] = 0
                    odd[nums[j]] += 1
                else:
                    if nums[j] not in even:
                        even[nums[j]] = 0
                    even[nums[j]] += 1
                if len(even) == len(odd):
                    out = max(out, j - i + 1)
            
            if nums[i] & 1:
                odd[nums[i]] -= 1
                if odd[nums[i]] == 0:
                    del odd[nums[i]]
            else:
                even[nums[i]] -= 1
                if even[nums[i]] == 0:
                    del even[nums[i]]
        return out