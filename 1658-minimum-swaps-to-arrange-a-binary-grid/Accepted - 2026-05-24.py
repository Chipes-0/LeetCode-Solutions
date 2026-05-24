class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        maxRight = []
        for row in grid:
            index = -1
            for i, num in enumerate(row):
                if num == 1:
                    index = i
            maxRight.append(index)

        out = 0 
        N = len(maxRight)
        for i in range(N - 1):
            for j in range(N - i - 1):
                if maxRight[j] > maxRight[j + 1]:
                   maxRight[j],  maxRight[j + 1] = maxRight[j + 1], maxRight[j]
                   out += 1
        for i in range(N):
            if maxRight[i] > i:
                return -1
        return out