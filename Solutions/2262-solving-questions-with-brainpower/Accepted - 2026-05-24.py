class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        dp = [0] * (N + 1) 
        for i in range(N - 1, -1, -1):
            if i + questions[i][1] + 1 > N:
                val = 0
            else:
                val = dp[i + questions[i][1] + 1]

            dp[i] = max(dp[i + 1], questions[i][0] + val)
        return dp[0]
            
