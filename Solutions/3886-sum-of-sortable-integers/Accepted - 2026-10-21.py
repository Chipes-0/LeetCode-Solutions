class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        N = len(nums)
        divisors = {n: [1, n] for n in range(1, N + 1)}
        divisors[1] = [1]
        for i in range(2, N + 1):
            for j in range(i * 2, N + 1, i):
                divisors[j].append(i)
        
        def valid(n):
            prev_max = float('-inf')
            for i in range(n, N + 1, n):
                block = nums[i - n : i]
                
                # Contar descensos en el bloque
                drops = 0
                drop_idx = -1
                for j in range(len(block) - 1):
                    if block[j] > block[j + 1]:
                        drops += 1
                        drop_idx = j
                
                if drops > 1:
                    return False
                
                if drops == 1:
                    # Si hay un descenso, el último elemento debe ser <= al primero
                    if block[-1] > block[0]:
                        return False
                    mn = block[drop_idx + 1]
                    mx = block[drop_idx]
                else:
                    mn = block[0]
                    mx = block[-1]

                if mn < prev_max:
                    return False
                prev_max = mx
            return True

        out = 0
        for div in divisors[N]:
            if valid(div):
                out += div
        return out