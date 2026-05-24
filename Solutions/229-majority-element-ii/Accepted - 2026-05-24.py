class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = int(len(nums) / 3)
        counters = {}
        output =[]
        for num in nums:
            if num not in counters:
                counters[num] = 1
            else:
                counters[num] += 1
        for key in counters:
            if counters[key] > n:
                output.append(key)
        return output