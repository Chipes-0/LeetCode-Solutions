class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def drawmap(row: int, col: int, cells: List[List[int]]) -> List[List[int]]:
            out = [[0] * col for i in range(row)]
            for cell in cells:
                r, c = cell
                out[r - 1][c - 1] = 1
            return out

        def canCross(row: int, col: int, mmap: List[List[int]]) -> bool:
            visited = set()
            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            visitq = [(0, cols) for cols in range(col) if mmap[0][cols] == 0]
            
            while visitq:
                r, c = visitq.pop()
                if r == row - 1:
                    return True
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                for dx, dy in moves:
                    nrow, ncol = r + dy, c + dx
                    if 0 <= nrow < row and 0 <= ncol < col and mmap[nrow][ncol] == 0:
                        visitq.append((nrow, ncol))
            return False

        low = 1
        high = row * col
        lastDay = 0
        while low <= high:
            m = (low + high) // 2
            mymap = drawmap(row, col, cells[:m])
            posible = canCross(row, col, mymap)
            print(low, high)
            if posible:
                low = m + 1
            else:
                high = m - 1
        return lastDay
