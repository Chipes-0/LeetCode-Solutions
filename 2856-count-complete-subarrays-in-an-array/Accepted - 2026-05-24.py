class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = set()
        for n in nums:
            distinct.add(n)
        k = len(distinct)

        left = 0
        count = 0
        out = 0
        d = defaultdict(int)
        for right in range(len(nums)):
            if not d[nums[right]]:
                count += 1
            d[nums[right]] += 1
            
            while count >= k:
                d[nums[left]] -= 1
                if not d[nums[left]]:
                    count -= 1
                left += 1
            out += left
        return out
