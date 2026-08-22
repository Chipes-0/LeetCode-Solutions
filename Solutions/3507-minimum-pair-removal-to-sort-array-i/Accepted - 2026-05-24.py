class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        out = 0
        stack = [nums[0]]
        curr = 0
        for n in nums:
            curr += n
            if curr >= stack[-1]:
                stack.append(curr)
                curr = 0
                continue
            out += 1
        
        return out
        
