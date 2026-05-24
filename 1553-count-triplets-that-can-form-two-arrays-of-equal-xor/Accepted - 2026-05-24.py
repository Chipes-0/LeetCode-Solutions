class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        out = 0
        for i in range(len(arr)):
            prefix_xor = arr[i]
            for j in range(i + 1, len(arr)):
                prefix_xor ^= arr[j]
                if prefix_xor == 0:
                    out += (j - i) 
        return out