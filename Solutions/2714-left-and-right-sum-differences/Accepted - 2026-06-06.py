class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ls, rs, out = [0], [0], [0] * N
        for i in range(N - 1):
            ls.append(nums[i] + ls[-1])
            rs.append(nums[N - 1 - i] + rs[-1])
        rs = rs[::-1]

        for i in range(N):
            out[i] = abs(ls[i] - rs[i])

        return out