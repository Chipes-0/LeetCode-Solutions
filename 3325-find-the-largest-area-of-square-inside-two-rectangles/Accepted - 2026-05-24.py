class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        out = 0
        ## comparar 2 rectangulos 
        for i in range(0, len(bottomLeft)):
            rec1 = (bottomLeft[i], topRight[i])
            for j in range(i + 1, len(bottomLeft)):
                rec2 = (bottomLeft[j], topRight[j])
                
                ## no intersectan
                # R1 esta a la izquierda de R2
                if rec1[1][0] <= rec2[0][0]:
                    continue
                # R1 esta a la derecha de R2
                elif rec2[1][0] <= rec1[0][0]:
                    continue
                # R1 esta arriba de R2
                elif rec2[1][1] <= rec1[0][1]:
                    continue
                # R1 esta abajo de R2
                elif rec1[1][1] <= rec2[0][1]:
                    continue
                
                # interseccion 
                x1, y1 = max(rec1[0][0], rec2[0][0]), max(rec1[0][1], rec2[0][1])
                x2, y2 = min(rec1[1][0], rec2[1][0]), min(rec1[1][1], rec2[1][1])

                width = x2 - x1
                heigh = y2 - y1
                out = max(out, min(width, heigh)**2)

        return out