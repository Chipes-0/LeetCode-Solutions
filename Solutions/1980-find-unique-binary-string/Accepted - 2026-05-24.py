class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums[0])
        combinations = 2 ** N
        seen = set()
        for num in nums:
            num = int(num,  2)
            seen.add(num)

        for i in range(combinations + 1):
            if i not in seen:
                return bin(i)[2:].zfill(N)
        return ""