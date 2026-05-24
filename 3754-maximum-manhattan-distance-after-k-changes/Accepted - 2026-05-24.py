class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        out = 0
        y = ["N", "S"]
        x = ["E", "W"]
        out = 0
        for i in range(2):
            for j in range(2):
                distance = 0
                changes = k
                for l in s:
                    if l == y[i] or l == x[j]:
                        distance += 1
                    elif changes:
                        distance += 1
                        changes -= 1
                    else:
                        distance -= 1
                    out = max(out, distance)
        return out