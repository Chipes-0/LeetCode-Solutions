class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        out = 0
        for num in reversed(s):
            if num == "0":
                count += 1
            else:
                out += count
        return out