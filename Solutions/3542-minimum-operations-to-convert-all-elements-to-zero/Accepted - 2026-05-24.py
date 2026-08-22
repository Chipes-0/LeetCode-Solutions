class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mstack = []
        out = 0

        for v in nums:
            while mstack and mstack[-1] > v:
                mstack.pop()
            if v == 0:
                continue
            if not mstack or mstack[-1] < v:
                mstack.append(v)
                out += 1
        return out
            