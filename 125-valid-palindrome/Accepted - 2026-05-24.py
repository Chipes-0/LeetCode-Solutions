import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s =  s.lower()
        s = ''.join(re.findall(r'[\w+]', s))
        return s == s[::-1]