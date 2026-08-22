class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        modulo = grid[0][0] % x
        nums = []
        for row in grid:
            for col in row:
                if col % x != modulo:
                    return -1
                nums.append(col)
        nums.sort()
        m = nums[len(nums)//2]
        out = 0
        for n in nums:
            out += abs(m - n) // x
        return out