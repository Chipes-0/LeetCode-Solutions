from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        suma = sum(piles)
        dp = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(2)]

        def points(player, left, right):
            if left > right:
                return 0 
            if dp[player][left][right] != - 1:
                return dp[player][left][right]

            if player:
                dp[player][left][right] = max(piles[left] + points(0, left + 1, right), piles[right] + points(0, left, right - 1))
            else:
                dp[player][left][right] = min(points(1, left + 1, right), points(1, left, right - 1))
            return dp[player][left][right]
        
        return points(1, 0, n - 1) > suma - points(1, 0, n - 1)