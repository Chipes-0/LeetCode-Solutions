class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index1 = 0
        index2 = 0
        output = ""
        for i in range(len(word1) + len(word2)):
            if index1 < len(word1):
                output += word1[index1]
                index1 += 1
            if index2 < len(word2):
                output += word2[index2]
                index2 += 1
                
        return output