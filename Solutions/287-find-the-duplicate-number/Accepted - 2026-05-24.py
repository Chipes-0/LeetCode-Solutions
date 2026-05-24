class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        slow = N - 1
        fast = N - 1

        while True:
            slow = nums[slow - 1]
            fast = nums[nums[fast - 1] - 1]
            print(slow, fast)
            if slow == fast:
                break
        finder = N - 1
        while True:
            slow = nums[slow - 1]
            finder = nums[finder - 1]

            if slow == finder:
                return slow

        return slow