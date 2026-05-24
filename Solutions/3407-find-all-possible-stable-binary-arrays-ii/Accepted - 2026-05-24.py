class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MODULO = 10 ** 9 + 7
        dp = [[[None for _ in range(2)] for _ in range(one + 1)] for _ in range(zero + 1)]
        def dfs(zeros, ones, next):
            # negative limit 
            if zeros < 0 or ones < 0:
                return 0
            # already in cache
            if dp[zeros][ones][next] != None:
                return dp[zeros][ones][next]
            result = 0
            
            # I only need to place ones without breaking the limit rule  
            if not zeros: 
                if next == 1 and ones <= limit:
                    result = 1
                dp[zeros][ones][next] = result
                return dp[zeros][ones][next]
            # I only need to place zeros without breaking the limit rule  
            elif not ones:
                if next == 0 and zeros <= limit:
                    result = 1
                dp[zeros][ones][next] = result
                return dp[zeros][ones][next]

            # I just added a Zero
            if next == 0:
                # Invalid equals to all remaining arrays that will break limit rule 
                invalid = dfs(zeros - limit - 1, ones, 1) % MODULO
                # get all posible arrays and subtract invalid ones
                result = (dfs(zeros - 1, ones, 0) + dfs(zeros - 1, ones, 1) - invalid + MODULO) % MODULO
            # i just added a One
            else:
                invalid = dfs(zeros, ones - limit - 1, 0) % MODULO
                result = (dfs(zeros, ones - 1, 0) + dfs(zeros, ones - 1, 1) - invalid + MODULO) % MODULO
            dp[zeros][ones][next] = result
            return dp[zeros][ones][next]

        return (dfs(zero, one, 0) + dfs(zero, one, 1)) % MODULO