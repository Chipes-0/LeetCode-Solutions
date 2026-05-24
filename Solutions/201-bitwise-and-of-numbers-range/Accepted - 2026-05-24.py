class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        out = left
        for i in range(left + 1, right + 1):
            out = out & i
            if out == 0:
                return 0
        return out