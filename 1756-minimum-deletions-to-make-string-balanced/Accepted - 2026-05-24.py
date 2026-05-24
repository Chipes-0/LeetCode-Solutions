class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        bs_before = [0] * (n + 1)
        as_after = [0] * (n + 1)
        v1, v2 = 0, 0
        for i in range(n):
            reverse = n - i - 1
            bs_before[i + 1] = bs_before[i] + v1            
            as_after[reverse] = as_after[reverse + 1] + v1

            if s[i] == "b":
                v1 = 1
                v2 = 0
            if s[reverse] == "a":
                v2 = 1
                v1 = 0
        out = float("inf")
        for i in range(n + 1):
            out = min(out, bs_before[i] + as_after[i])
        return out
