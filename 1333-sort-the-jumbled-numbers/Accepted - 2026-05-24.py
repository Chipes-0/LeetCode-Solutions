class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped = {}
        for element in nums:
            copy = list(str(element))
            num = 0
            for i in range(len(copy)):
                num += mapping[int(copy[i])]
                num *= 10
            mapped[element] = num
        return [x for x, y in sorted(mapped.items(), key=lambda item: item[1])]