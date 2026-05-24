from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        for s in strs:
            val = sum([ord(i) for i in s])
            dd[val].append(s)
        return dd.values()
            