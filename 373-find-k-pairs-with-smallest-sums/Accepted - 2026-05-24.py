from collections import defaultdict
import collections

class Solution:
    out = []
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:   
        d = defaultdict(list)
        for n in range(len(nums1)):
            for m in range(len(nums2)):
                d[nums2[m] + nums1[n]].append([nums1[n], nums2[m]])
        
        od = dict(collections.OrderedDict(sorted(dict(d).items())))
        out = []
        for key in od:
            for pair in od[key]:
                if k:
                    out.append(pair)
                    k -= 1
                else:
                    break

        return out
    