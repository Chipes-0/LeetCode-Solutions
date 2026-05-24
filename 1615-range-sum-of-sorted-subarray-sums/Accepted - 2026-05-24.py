class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        n = len(nums)
        MODULO = 10**9 + 7
        sums = []
        for i in range(n):
            sum_acum = 0
            for j in range(i, n):
                sum_acum += nums[j] % MODULO
                sums.append(sum_acum)
        sums.sort()
        return sum(sums[left-1:right]) % MDOULO