class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                break
            while s[left + 1] == s[right] and left + 1 < right:
                left += 1
            while s[right - 1] == s[left] and right - 1 > left:
                right -= 1
            left += 1
            right -= 1
        return right - left + 1 