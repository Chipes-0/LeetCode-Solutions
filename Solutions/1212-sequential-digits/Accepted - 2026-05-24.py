class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        out = []
        def sequence(num, next):
            if num > high or next == 11:
                return 
            if num > low:
                out.append(num)
            next = num % 10 + 1
            sequence(num * 10 + next, + next + 1)
        for i in range(1, 10):
            sequence(i, i + 1)
        return sorted(out)
