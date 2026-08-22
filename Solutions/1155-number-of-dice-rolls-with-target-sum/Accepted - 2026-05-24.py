class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7
        if n * k  < target:
            return 0
        dp = [[None] * (target + 1) for _ in range(n + 1)]

        def rollDice(n_dice, target_sum):
            if n_dice == 0:
                return 1 if target_sum == 0 else 0
            if target_sum < 0:
                return 0
            if dp[n_dice][target_sum] is not None:
                return dp[n_dice][target_sum]
            total_ways = 0
            limit = min(k, target)
            for i in range(1, limit + 1):
                total_ways += rollDice(n_dice - 1, target_sum - i) % mod
            dp[n_dice][target_sum] = total_ways
            return total_ways % mod
            
        ans = rollDice(n, target)
        return ans % mod
        