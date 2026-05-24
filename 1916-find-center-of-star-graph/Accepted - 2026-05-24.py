from collections import defaultdict

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        df = defaultdict(int)
        for pair in edges:
            df[pair[0]] += 1
            df[pair[1]] += 1
            if df[pair[0]] > 1:
                return pair[0]
            if df[pair[1]] > 1:
                return pair[1]
            