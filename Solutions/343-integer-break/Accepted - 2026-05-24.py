class Solution:
    def integerBreak(self, n: int) -> int:
        max = 1
        for i in range(1, n):
            if i % 3 == 0:
                if pow(3, i // 3) * (n - i) > max:
                    max = pow(3, i // 3) * (n - i)
            if i * (n - i) > max:
                max = i * (n - i)
        return max
        