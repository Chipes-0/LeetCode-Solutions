class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        q = [0, 0]
        sums = [0, 0]
        for i, ch in enumerate(num):
            side = i // (n // 2)
            if ch == "?":
                q[side] += 1
            else:
                sums[side] += int(ch)

        if sum(q) & 1:
            return True

        ## Se puede anular la misma cantidad de ? en izquierda y derecha
        q_diff = q[0] - q[1]
        ## la diferencia de sumas es lo que hay que conseguir 
        sum_diff = sums[0] - sums[1]
        
        ## la -9 para inidicar que la diferencia debe estar en el otro lado 
        ## cada 2 preguntas podemos balancear a que haya un 9
        return sum_diff != (-9 * q_diff // 2) 
        
