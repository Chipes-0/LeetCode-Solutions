class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack  = []
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                v = stack.pop()
                max_area = max((i - v[0]) * v[1], max_area)
                start = v[0]
            stack.append((start, h))
        while stack:
            v = stack.pop()
            max_area = max((i + 1 - v[0]) * v[1], max_area)
        return max_area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        N = len(matrix[0])
        histogram = [0] *  N
        max_area = 0
        for i in range(len(matrix)):
            for j in range(N):
                if matrix[i][j] == "0":
                    histogram[j] = 0
                else:
                    histogram[j] += int(matrix[i][j])
            max_area = max(max_area, self.largestRectangleArea(histogram))
        return max_area