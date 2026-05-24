class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        k = m + n
        total = (mean * k) - sum(rolls)
        out = []
        if total > 6 * n:
            return out
        distributedmean = total // n
        mod = total % n
        for _ in range(n):
           out.append(distributedmean)
        for i in range(mod):
            out[i] += 1
        return out
