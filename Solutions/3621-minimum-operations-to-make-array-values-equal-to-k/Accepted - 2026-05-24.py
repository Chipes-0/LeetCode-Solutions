class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = set()
        out = 0
        flag = True
        for n in nums:
            if n > k and n not in s:
                out += 1
                flag = False
                s.add(n)
        if flag:
            return -1
        return out