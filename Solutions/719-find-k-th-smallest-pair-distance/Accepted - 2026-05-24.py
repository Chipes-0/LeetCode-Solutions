class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        right = nums[-1] - nums[0]
        left = 0
        while left < right:
            m = (right + left) // 2
            count = 0
            flag = False
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[j] - nums[i] <= m:
                        count += 1
                    if count >= k:
                        flag = True
                        break
                if flag:
                    break
            if flag:
                right = m - 1
            else:
                left = m + 1
        return left