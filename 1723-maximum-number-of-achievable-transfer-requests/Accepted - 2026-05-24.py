from collections import defaultdict

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        d = defaultdict(int)
        out = len(requests)
        for req in requests:
            d[req[0]] -= 1
            d[req[1]] += 1
        print(d)
        for v in d.values():
            if v != 0:
                out -= abs(0.5 * v)
        return int(out)
