class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                mmax_depth = max(max_depth, )