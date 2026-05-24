class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        repeated_letters = []
        max_substring = 0
        for l in s:
            if l not in repeated_letters:
                length += 1
                repeated_letters.append(l)
            else:
                if length > max_substring:
                    max_substring = length 
                repeated_letters = []
                repeated_letters.append(l)
                length = 1
        return max_substring