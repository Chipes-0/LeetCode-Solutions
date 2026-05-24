class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        start = end = ""
        while left < right:
            if s[left] not in "aeiou":
                start += s[left]
                left += 1
            if s[right] not in "aeiou":
                end = s[right] + end
                
            start += s[right]
            end = s[left] + end
            
            
            print(start, end)
        return start 