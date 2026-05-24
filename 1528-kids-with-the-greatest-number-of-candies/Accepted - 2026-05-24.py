class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        M = max(candies)
        l2 = []
        for e in candies:
            if e + extraCandies >= M:
                l2.append(True)
            else:
                l2.append(False)

        return l2