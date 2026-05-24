class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.ps = [0]
        for num in self.nums:
            self.ps.append(self.ps[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.ps[right + 1] - self.ps[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)