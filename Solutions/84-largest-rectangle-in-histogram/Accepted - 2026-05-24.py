class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack  = []
        max_area = 0
        for i, h in enumerate(heights):
            if not stack:
                stack.append((i, h))
                max_area = h
                continue
            else:
                while stack and stack[-1][1] > h:
                    v = stack.pop()
                    
            stack.append((i, h))
            
        return max_area

            