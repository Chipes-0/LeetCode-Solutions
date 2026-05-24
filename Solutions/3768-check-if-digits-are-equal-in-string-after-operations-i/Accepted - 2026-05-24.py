class Solution:
    def hasSameDigits(self, s: str) -> bool:
        l = list(map(int, list(s)))
        while len(l) != 2:
            for i in range(len(l) - 1):
                l[i] = (l[i] + l[i+1]) % 10
            l.pop(-1)

        return l[0] == l[1]