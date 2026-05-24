class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MODULO = 10 ** 9 + 7
        dp = [[[None for _ in range(2)] for _ in range(one + 1)] for _ in range(zero + 1)]
        def dfs(zeros, ones, next):
            # negative limit 
            if zeros < 0 or ones < 0:
                return 0

            if dp[zeros][ones][next] != None:
                return dp[zeros][ones][next]
            result = 0
            if not zeros: 
                if next == 1 and ones <= limit:
                    result = 1
                dp[zeros][ones][next] = result
                return dp[zeros][ones][next]
            if not ones:
                if next == 0 and zeros <= limit:
                    result = 1
                dp[zeros][ones][next] = result
                return dp[zeros][ones][next]

            if next == 0:
                invalid =(dfs(zeros - limit - 1, ones, 1) + dfs(zeros - limit - 1, ones, 0)) % MODULO
                result = dfs(zeros - 1, ones, 0) + dfs(zeros - 1, ones, 1) - invalid
            elif next == 1:
                invalid = (dfs(zeros, ones - limit - 1, 1) + dfs(zeros, ones - limit - 1, 0)) % MODULO
                result = dfs(zeros, ones - 1, 0) + dfs(zeros, ones - 1, 1) - invalid
            dp[zeros][ones][next] = result
            return dp[zeros][ones][next]
        return (dfs(zero, one, 0) + dfs(zero, one, 1)) % MODULO