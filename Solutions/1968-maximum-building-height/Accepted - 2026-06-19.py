class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])
        N = len(restrictions)
        for i in range(1, N):
            x2, h2 = restrictions[i]
            x1, h1 = restrictions[i - 1]

            restrictions[i][1] = min(h2, h1 + (x2 - x1))
        
        for i in range(N - 2, -1, -1):
            x2, h2 = restrictions[i + 1]
            x1, h1 = restrictions[i]

            restrictions[i][1] = min(h1, h2 + (x2 - x1))

        out = 0
        for i in range(1, N):
            x1, h1 = restrictions[i - 1]
            x2, h2 = restrictions[i]

            distance = x2 - x1
            peak = (h1 + h2 + distance) // 2
            out = max(out, peak)
        return out
        