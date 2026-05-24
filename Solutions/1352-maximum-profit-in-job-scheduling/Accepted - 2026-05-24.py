class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(list(zip(startTime, endTime, profit)), key=lambda x: x[0])
        N = len(jobs)
        dp = {}
        
        def backtracking(i):
            nonlocal dp
            if i == N:
                return 0
            if i in dp:
                return dp[i]
            # don't take the job
            ans = backtracking(i + 1)
            # take it
            j = i + 1
            while j < N and not jobs[i][1] <= jobs[j][0]:
                j += 1
            ans = max(ans, jobs[i][2] + backtracking(j))
            dp[i] = ans
            return ans
        return backtracking(0)