class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        hm = {}
        for w in s1:
            if w not in hm:
                hm[w] = 1
            else:
                hm[w] += 1

        for w in s2:
            if w not in hm:
                hm[w] = 1
            else:
                hm[w] += 1
        out = []
        for w in hm.keys():
            if hm[w] == 1:
                out.append(w)
        return out