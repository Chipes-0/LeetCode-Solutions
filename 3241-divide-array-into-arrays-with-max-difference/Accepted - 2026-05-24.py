class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        out = []
        add = [nums[0]]
        for i in range(1, len(nums)):
            if len(add) == 3:
                out.append(add)
                add = []
            if not add:
                add.append(nums[i])
            elif abs(add[-1] - nums[i]) <= k:
                add.append(nums[i])
            else:
                return []
        out.append(add)
        return out