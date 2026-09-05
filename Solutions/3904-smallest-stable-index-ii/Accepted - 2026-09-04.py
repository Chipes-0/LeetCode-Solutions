class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        N = len(nums)
        mina, maxa = [nums[-1]] * N, [nums[0]] * N
        for i in range(1, N):
            maxa[i] = max(maxa[i - 1], nums[i])
            mina[N - 1 - i] = min(mina[N - i], nums[N - 1 - i])
        
        for i in range(N):
            if maxa[i] - mina[i] <= k:
                return i
        return -1