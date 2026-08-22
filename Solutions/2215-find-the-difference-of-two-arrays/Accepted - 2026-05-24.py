class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nnums1 = []
        nnums2 = []
        for i in range(len(nums1)):
            if nums1[i] not in nums2 and nums1[i] not in nnums1:
                nnums1.append(nums1[i])

        for i in range(len(nums2)):
            if nums2[i] not in nums1 and nums2[i] not in nnums2:
                nnums2.append(nums2[i])
                
        return [nnums1, nnums2]