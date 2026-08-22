from collections import defaultdict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        df = defaultdict(int)
        m, M = float("inf"), 0
        for n in hand:
            df[n] += 1
            if n < m:
                m = n
            if n > M:
                M = n
        for i in range(m, M + 1):
            while df[i]:
                for j in range(i, i + groupSize):
                    if not df[j]:
                        return False
                    df[j] -= 1
        return True