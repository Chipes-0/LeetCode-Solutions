class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def prime(n):
            if n > 1:
                for i in range(2, (n//2)+1):
                    if (n % i) == 0:
                        return "0"
            return "1"

        array = ''.join(list(map(prime, nums)))
        return array.rfind("1") - array.find("1")