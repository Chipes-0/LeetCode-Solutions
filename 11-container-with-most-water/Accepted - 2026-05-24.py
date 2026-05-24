class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(area, max_area)
            print(area)
            if height[left + 1] > height[right - 1]:
                left += 1
            else:
                right -= 1
        return max_area