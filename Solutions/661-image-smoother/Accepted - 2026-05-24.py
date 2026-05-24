import math 

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        cols, rows = len(img[0]), len(img)
        out = []
        for i in range(rows):
            out.append([])
            for j in range(cols):
                actual_sum = 0
                for x in range(max(0, i - 1), min(rows, i + 2)):
                    for y in range(max(0, j - 1), min(cols, j + 2)):
                        actual_sum += img[x][y]
                div = 4 if i in (0, rows - 1) and j in (0, cols - 1) else \
                6 if i in (0, rows - 1) or j in (0, cols - 1) else 9
                actual_sum /= div
                out[i].append(math.floor(actual_sum))
        return out