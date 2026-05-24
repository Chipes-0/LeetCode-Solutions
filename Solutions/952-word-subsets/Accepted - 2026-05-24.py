class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = [0] * 26
        for w in words2:
            freq = [0] * 26
            for c in w:
                freq[ord(c) - ord('a')] += 1
            for i in range(26):
                max_freq[i] = max(max_freq[i], freq[i])
        out = []
        for w in words1:
            freq = [0] * 26
            for c in w:
                freq[ord(c) - ord('a')] += 1
            skip = False
            for i in range(26):
                if freq[i] < max_freq[i]:
                    skip = True
                    break
            if skip:
                continue
            out.append(w)
        return out