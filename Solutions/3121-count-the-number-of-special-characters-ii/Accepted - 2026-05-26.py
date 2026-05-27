class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first = [-1] * 26
        last = [-1] * 26

        for i in range(len(word)):
            if word[i] >= 'A' and word[i] <= 'Z' and first[ord(word[i]) - ord('A')] == -1:
                first[ord(word[i]) - ord('A')] = i
            
            if word[i] >= 'a' and word[i] <= 'z':
                last[ord(word[i]) - ord('a')] = i

        out = 0
        for i in range(26):
            if first[i] != -1 and last[i] != -1:
                out += 1 if last[i] < first[i] else 0
        return out