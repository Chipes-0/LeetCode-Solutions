class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        ans = 0
        earlier = float('-inf')
        for start, end in pairs:
            if start > earlier:
                ans += 1
                earlier = end
        return ans