class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        N = len(seq)
        out = [0] * N
        stack = 0
        for i, ch in enumerate(seq):
            if ch == "(":
                stack += 1
                out[i] = stack % 2
            else:
                out[i] = stack % 2
                stack -= 1
        return out