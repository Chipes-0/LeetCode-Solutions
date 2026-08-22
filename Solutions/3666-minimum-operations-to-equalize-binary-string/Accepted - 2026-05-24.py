class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        zeros, ones = 0, 0
        for digit in s:
            if digit == "0":
                zeros += 1
            else:
                ones += 1
        
        for op in range(1, n + 1):
            flips = k * op
            if (flips - zeros) & 1:
                continue
            if op & 1:
                if zeros <= flips <= (zeros * op) + (ones * (op - 1)):
                    return op
                
            else:
                if zeros <= flips <= (zeros * (op - 1)) + (ones * op):
                    return op
        return -1