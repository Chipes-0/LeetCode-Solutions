class Solution:
    def longestValidParentheses(self, s: str) -> int:
        N = len(s)

        def check(string, open_ch):
            out = 0
            left = 0
            curr = 0
            for right in range(len(string)):
                curr += 1 if string[right] == open_ch else -1

                if curr < 0:
                    curr = 0
                    left = right + 1
                if curr == 0:
                    out = max(out, right - left + 1)
            return out
        return max(check(s, "("), check(s[::-1], ")"))