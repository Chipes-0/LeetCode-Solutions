class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        squares = [1]
        val = 4
        num = 2
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            if i == val:
                squares.append(val)
                num += 1
                val = num * num
            flag = False
            for sq in squares:
                if not dp[i - sq]:
                    flag = True
                    break
            dp[i] = flag

        return dp[n]