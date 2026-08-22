class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MODULO = 10**9 + 7
        rango = r - l + 1

        curr_up = [1] * rango
        curr_down = [1] * rango

        for _ in range(1, n):
            next_down = [0] * rango
            next_up = [0] * rango
            

            sufixSum = 0
            for val in range(rango - 2, -1, -1):
                sufixSum += curr_up[val + 1]
                next_down[val] = sufixSum


            prefixSum = 0
            for val in range(1, rango):
                prefixSum += curr_down[val - 1] 
                next_up[val] = prefixSum
            
            curr_up = [x % MODULO for x in next_up]
            curr_down = [x % MODULO for x in next_down]
                    
        out = 0
        for i in range(rango):
            out += curr_down[i] % MODULO
            out += curr_up[i] % MODULO
        return out % MODULO