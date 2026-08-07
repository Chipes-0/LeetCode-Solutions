from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        suma = sum(nums)
        dp = [[[0 for n in range(n)] for _ in range(n)] for _ in range(2)]
        # [player][left][right]

        def predict(turn, left, right):
            if left > right:
                return 0
            if dp[turn][left][right]:
                return dp[turn][left][right]
            if turn:
                dp[turn][left][right] = max(nums[left] + predict(0, left + 1, right), nums[right] + predict(0, left, right - 1))
            else:
                dp[turn][left][right] = min(predict(1, left + 1, right), predict(1, left, right - 1))

            return dp[turn][left][right]

        return predict(1, 0, n - 1) >= predict(0, 0, n - 1)