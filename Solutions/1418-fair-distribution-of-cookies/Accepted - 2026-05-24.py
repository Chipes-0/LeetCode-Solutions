import math

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        kids = [0] * k
        ans = math.inf

        def fcookies(index: int, kids: List[int]) -> None:
            nonlocal ans
            if index == len(cookies):
                ans = min(ans, max(kids))
                return
            for i in range(k):
                kids[i] += cookies[index]
                fcookies(index + 1, kids)
                kids[i] -= cookies[index]
        fcookies(0, kids)
        return ans
