class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [float("inf")] * n
        arr[0] = 0

        for i in range(n - 1):
            for j in range(i + nums[i]):
                if i + j + 1 > n:
                    break
                arr[j+1] = min(arr[j+1], arr[i] + 1)
        
        return arr[-1]