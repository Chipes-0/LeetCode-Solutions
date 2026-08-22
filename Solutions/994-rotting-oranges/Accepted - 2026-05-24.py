class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        oranges = 0
        queue = []
        seen = set()
        up, down = 0, len(grid)
        left, right = 0, len(grid[0])
        for i in range(down):
            for j in range(right):
                if grid[i][j] == 1:
                    oranges += 1
                elif grid[i][j] == 2:
                    oranges += 1
                    queue.append((i, j, 0))

        adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        out = 0
        while queue:
            row, col, minutes = queue.pop()
            seen.add((row, col))
            out = max(out, minutes)
            oranges -= 1
            for dy, dx in adj:
                newx, newy = row + dy, col + dx
                if newy >= up and newy < down and newx >= left and newx < right:
                    if (newy, newx) not in seen and grid[newy][newx] == 1:
                        queue.append((newy, newx, minutes + 1))
                        seen.add((newy, newx))
    
        if oranges:
            return -1
        return out