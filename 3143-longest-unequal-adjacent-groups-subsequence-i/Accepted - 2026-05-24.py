class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        out = [words[0]]
        last = groups[0]
        for i in range(1, len(words)):
            if last != groups[i]:
                last = groups[i]
                out.append(words[i])
        return out