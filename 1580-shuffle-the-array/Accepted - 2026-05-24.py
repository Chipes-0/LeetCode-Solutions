class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        x = 0
        y = n
        out = []
        for i in range(2 * n):
            if i % 2 == 0:
                out.append(nums[x])
                x += 1
            else:
                out.append(nums[y])
                y += 1
        return out