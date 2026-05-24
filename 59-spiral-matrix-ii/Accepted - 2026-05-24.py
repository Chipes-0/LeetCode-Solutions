class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        out = [[0 for _ in range(n)] for _ in range(n)]
        left, right = 0, n - 1
        top, down = 0, n - 1

        i = 1
        while left <= right and top <= down:
            # izquierda a derecha
            for col in range(left, right + 1):
                out[top][col] = i
                i += 1
            top += 1
            # arriba a abajo
            for row in range(top, down + 1):
                out[row][right] = i
                i += 1
            right -= 1
            # derecha a izquierda
            for col in range(right, left - 1, -1):
                out[down][col] = i
                i += 1
            down -=1
            # abajo a arriba
            for row in range(down, top - 1, -1):
                out[row][left] = i
                i += 1
            left +=1

        return out