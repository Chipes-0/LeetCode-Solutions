class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old = image[sr][sc]
        adjacent  = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = [(sr, sc)]
        top, down, left, right = 0, len(image), 0, len(image[0])
        seen = {(sr, sc)}

        while queue:
            row, col = queue.pop(0)
            image[row][col] = color
            for ad in adjacent:
                dx, dy = ad
                rowy, colx = row + dx, col + dy
                if rowy >= top and rowy < down and colx >= left and colx < right:
                    if image[rowy][colx] == old and (rowy, colx) not in seen:
                        queue.append((rowy, colx))
                        seen.add((rowy, colx))
        return image