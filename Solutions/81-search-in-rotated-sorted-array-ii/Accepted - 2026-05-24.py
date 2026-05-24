class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        pivot = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                pivot = i
                break

        left, right = 0, pivot
        while left <= right:
            m = (left + right) // 2
            if nums[m] == target:
                return True
            elif nums[m] < target:
                left = m + 1
            else:
                right = m - 1
        left, right = pivot, len(nums) - 1

        while left <= right:
            m = (left + right) // 2
            if nums[m] == target:
                return True
            elif nums[m] < target:
                left = m + 1
            else:
                right = m - 1
        return False