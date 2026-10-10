class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        N = len(nums1)
        k = k1 + k2
        diffs = []

        for i in range(N):
            diffs.append(abs(nums1[i] - nums2[i]))
        diffs.sort(reverse = True)
        
        if sum(diffs) <= k:
            return 0

        diffs.append(0)

        for i in range(N):
            count = i + 1
            dif = diffs[i] - diffs[i + 1]
            need = dif * count # aplanar de mayor a menor

            if k >= need:
                k -= need
            else:
                level, rem = k // count, k % count
                val = diffs[i] - level
                out = rem * (val - 1) ** 2
                out += (count - rem) * val ** 2
                
                for j in range(i + 1, N):
                    out += diffs[j] ** 2
                return out
        return 0