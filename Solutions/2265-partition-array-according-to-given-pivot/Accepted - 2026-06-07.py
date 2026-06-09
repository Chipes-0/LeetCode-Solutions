class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        larger = []
        pivotCounts = 0
        
        for num in nums:
            if num == pivot:
                pivotCounts += 1
            elif num < pivot:
                smaller.append(num)
            else:
                larger.append(num)
                
        
        out = smaller + [pivot] * pivotCounts + larger
        return out