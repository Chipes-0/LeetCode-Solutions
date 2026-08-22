class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hash_map = {}
        for i, s in enumerate(arr):
            if s in hash_map:
                hash_map[s] = -1
            else:
                hash_map[s] = i
        for key, v in hash_map.items():
            if v != -1:
                k -= 1
            if k == 0:
                return key
        return ""