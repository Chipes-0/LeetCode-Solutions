class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[[0 for _ in range(2)] for _ in range(n)] for _ in range(n)]
        def predict(left, right, turn) -> int:
            if left > right:
                return 0
            if dp[left][right][turn]:
                return dp[left][right][turn]
            
            ans = 0
            if turn:
                ans = max(nums[left] + predict(left + 1, right, 0), nums[right] + predict(left, right - 1, 0))
            else:
                ans = min(predict(left + 1, right, 1), predict(left, right - 1, 1))
            dp[left][right][turn] = ans
            return dp[left][right][turn]
        
        points = predict(0, n - 1, 1)
        return points >= sum(nums) / 2