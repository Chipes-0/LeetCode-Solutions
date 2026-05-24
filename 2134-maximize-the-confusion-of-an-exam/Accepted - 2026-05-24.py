from collections import defaultdict

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        maxconf = 0
        array = ['T', 'F']
        if all(element == 'T' for element in answerKey) or all(element == 'F' for element in answerKey):
            return len(answerKey)
        for res in array:
            left = corrections = 0
            for right in range(len(answerKey)):
                if answerKey[right] != res:
                    corrections += 1
                while corrections > k:
                    if answerKey[left] != res:
                        corrections -= 1
                    left += 1
                maxconf = max(maxconf, right - left + 1)
        return maxconf
                
