class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MODULO = 10**9 + 7
        rango = r - l + 1

        def multiply(A, B):
            n = len(A)
            C = [[0] * n for _ in range(n)]

            for i in range(n):
                for k in range(n):
                    if A[i][k] == 0:
                        continue
                    for j in range(n):
                        if B[k][j] == 0:
                            continue
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MODULO

            return C
        
        def identity_matrix(n):
            I = [[0] * n for _ in range(n)]

            for i in range(n):
                I[i][i] = 1

            return I

        def matrix_power(base, exp):
            n = len(base)
            result = identity_matrix(n)

            while exp > 0:
                if exp & 1:
                    result = multiply(result, base)

                base = multiply(base, base)
                exp >>= 1

            return result

        SIZE = 2 * rango
        M = [[0] * SIZE for _ in range(SIZE)]
        ## Construir matriz de transiciones 
        MENOR = 0
        MAYOR = 1

        for i in range(rango):
            for j in range(rango):

                ## Sigue un Menor
                if j < i:
                    from_state = i * 2 + MENOR
                    to_state = j * 2 + MAYOR
                    M[from_state][to_state] = 1

                ## Sigue un Mayor
                if j > i:
                    from_state = i * 2 + MAYOR
                    to_state = j * 2 + MENOR
                    M[from_state][to_state] = 1

        P = matrix_power(M, n - 1)
        out = 0
        for row in P:
            for num in row:
                out += num
                out %= MODULO
        return out
