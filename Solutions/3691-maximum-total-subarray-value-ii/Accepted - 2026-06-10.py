from heapq import heappush, heappop
from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        N = len(nums)
        M = N.bit_length()

        def build_sparse_table(nums, isMin):
            op = min if isMin else max
            st = [[0] * N for _ in range(M)]

            for i in range(N):
                st[0][i] = nums[i]

            for j in range(1, M):
                length = 1 << j

                for i in range(N - length + 1):
                    st[j][i] = op(st[j - 1][i], st[j - 1][i + (length >> 1)])
            return st
        
        def query(st, l, r, isMin):
            K = (r - l + 1).bit_length() - 1
            op = min if isMin else max
            return op(st[K][l], st[K][r - (1 << K) + 1])

        minST = build_sparse_table(nums, True)
        maxST = build_sparse_table(nums, False)
        
        def value(l, r):
            minVal = query(minST, l, r, True)
            maxVal = query(maxST, l, r, False)
            return maxVal - minVal

        heap = []
        for l in range(N):
            heappush(heap, (-value(l, N - 1), l, N - 1))
            
        out = 0
        while k:
            val, l, r = heappop(heap)
            out -= val
            if r > l:
                heappush(heap, (-value(l, r - 1), l, r - 1))
            k -= 1
        return out