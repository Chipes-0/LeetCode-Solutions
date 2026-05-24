from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = defaultdict(int)
        array = []
        for num in nums:
            if num not in array:
                array.append(num)
            d[num] += 1
            if d[num] == 2:
                array.remove(num)
        return array[0]
        