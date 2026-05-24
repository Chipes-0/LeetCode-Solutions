class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        prefix_sum = [1]
        for i in range(2, n + 1):
            prefix_sum.append(i + prefix_sum[-1])
        for i in range(n):
            if prefix_sum[i] == prefix_sum[-1] - prefix_sum[i - 1]:
                return i + 1
        return -1