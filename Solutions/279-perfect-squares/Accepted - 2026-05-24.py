import math

class Solution:
    def numSquares(self, n: int) -> int:
        def perfectsqr(num):
            return math.sqrt(num) == math.sqrt(num) // 1
        
        squares = []
        for i in range(1, n + 1):
            if perfectsqr(i):
                squares.append(i)
        squares = squares[::-1]

        dp = [float("inf") for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(len(squares)):
                if squares[j] <= i:
                    aux = dp[i - squares[j]]
                    if aux != float("inf") and aux + 1 < dp[i]:
                        dp[i] = aux + 1               
        return dp[n]

