class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        module = pow(10, 9) + 7
        def ways(numsarr):
            if len(numsarr) <= 2:
                return 1
            root = numsarr[0]

            leftarr = [num for num in numsarr if num < root]
            rightarr = [num for num in numsarr if num > root]

            return ways(leftarr) * ways(rightarr) * comb(len(numsarr) - 1, len(leftarr))
        return (ways(nums) - 1) % module
