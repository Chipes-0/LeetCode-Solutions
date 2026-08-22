class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = [0] * 26
        for c in words[0]:
            common[ord(c) - ord('a')] += 1
        for word in range(1, len(words)):
            current = [0] * 26
            for c in words[word]:
                current[ord(c) - ord('a')] += 1
            
            for i in range(26):
                common[i] = min(current[i], common[i])

        out = []
        for i in range(26):
            for _ in range(common[i]):
                out.append(chr(i + ord('a')))
        return out