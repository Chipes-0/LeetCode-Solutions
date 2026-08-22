class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        out = ""
        for w in words:
            curr = 0
            for ch in w:
                curr += weights[ord(ch) - ord('a')]
            out += chr(ord('z') - (curr % 26))
        return out