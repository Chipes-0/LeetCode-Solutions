class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        total = 0
        Lmax = Rmax = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > Lmax:
                    Lmax = height[left]
                else:
                    total += Lmax - height[left]
                left += 1
            else:
                if height[right] > Rmax:
                    Rmax = height[right]
                else:
                    total += Rmax - height[right]
                right -= 1
        return total