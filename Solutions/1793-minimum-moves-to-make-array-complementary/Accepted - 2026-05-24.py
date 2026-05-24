class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        N = len(nums)
        pairs = N // 2

        diff = [0] * (2 * limit + 2)

        for i in range(pairs):
            a = nums[i]
            b = nums[N - 1 - i]

            x = min(a, b)
            y = max(a, b)

            # 2 -> 1 movimientos
            diff[x + 1] -= 1
            diff[y + limit + 1] += 1

            # 1 -> 0 movimientos
            s = a + b
            diff[s] -= 1
            diff[s + 1] += 1

        out = float('inf')
        curr = N
        
        for target in range(2 * limit + 2):
            curr += diff[target]
            out = min(out, curr)

        return out