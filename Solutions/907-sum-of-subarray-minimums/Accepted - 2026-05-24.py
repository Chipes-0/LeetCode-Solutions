class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        modulo = 10 ** 9 + 7
        N = len(arr)
        out = 0
        stack = []
        prev = [0] * N
        for i, val in enumerate(arr):
            prev_i = i
            while stack and stack[-1][1] >= val:
                prev_i, _ = stack.pop()
            prev[i] = i - prev_i + 1
            stack.append((prev_i, val))
        stack = []
        next = [0] * N
        for i, val in enumerate(arr[::-1]):
            next_i = i
            while stack and stack[-1][1] > val:
                next_i, _ = stack.pop()
            next[i] = i - next_i + 1
            stack.append((next_i, val))
        next  = next[::-1]

        for i in range(N):
            out += next[i] * prev[i] * arr[i]
        return out % modulo