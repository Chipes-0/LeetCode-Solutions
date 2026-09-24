class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        N = len(nums)
        total = sum(nums)
        target = total - x

        if total == x:
            return N

        out = -1
        curr = 0
        left = 0
        for right in range(N):
            curr += nums[right]
            while curr >= target and left < right:
                if curr == target:
                    out = max(out, right - left + 1) if out != -1 else right - left + 1
                curr -= nums[left]
                left += 1
            if curr == target:
                out = max(out, right - left + 1) if out != -1 else right - left + 1
        
        if out == -1:
            return out
        return N - out