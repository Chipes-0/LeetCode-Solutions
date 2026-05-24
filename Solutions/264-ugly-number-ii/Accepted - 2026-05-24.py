class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1 for _ in range(n)]
        two, three, five = 0,0,0
        v2, v3, v5 = 2, 3, 5
        for i in range(1, n):
            dp[i] = min(v2,v3,v5)
            if dp[i] == v2:
                two += 1
                v2 = dp[two] * 2
            if dp[i] == v3:
                three += 1
                v3 = dp[three] * 3
            if dp[i] == v5:
                five += 1
                v5 = dp[five] * 5
        return dp[n - 1]
                
