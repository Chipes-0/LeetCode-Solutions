from typing import List
import copy

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        index_c = {}
        # O(N)
        for i in range(len(s)):
            character = s[i]
            if character not in index_c:
                index_c[character] = []
            index_c[character].append(i)

        out = 0
        def isSubSeq(word, indexes):
            index = -1
            for character in word:
                if character not in indexes or not indexes[character]:
                    return False
                while indexes[character]:
                    if index < indexes[character][0]:
                        index = indexes[character].pop(0)
                        break
                    indexes[character].pop(0)
                    if not indexes[character]:
                        return False
            return True
        
        for word in words:
            if isSubSeq(word, copy.deepcopy(index_c)):
                out += 1
        return out