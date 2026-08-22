from bisect import bisect_left

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        class Fenwick:
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)

            def update(self, idx, delta):
                while idx <= self.n:
                    self.bit[idx] += delta
                    idx += idx & -idx

            def query(self, idx):
                s = 0
                while idx > 0:
                    s += self.bit[idx]
                    idx -= idx & -idx
                return s
        
        N = len(nums)
        nums = [1 if x == target else -1 for x in nums]
        psum = [0]
        for i in range(N):
            psum.append(psum[-1] + nums[i])

        ranks = list(sorted(set(psum)))
        def rank(num):
            return bisect_left(ranks, num) + 1

        FT = Fenwick(len(ranks))
        FT.update(rank(0), 1)
        out = 0
        for i in range(N):
            r = rank(psum[i + 1])
            out += FT.query(r - 1)
            FT.update(r, 1)
        return out
