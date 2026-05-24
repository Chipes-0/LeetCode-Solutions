class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ""
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                temp = s[i:j]
                if temp == temp[::-1]:
                    if len(temp) > len(output):
                        output = temp
        return output

                    
