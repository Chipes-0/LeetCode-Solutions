class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5
        l1 = [1, 1, 1, 1, 1]
        l2 = [1]
        while n - 2 > 0:
            for i in range(1, 5):
                a = l2[-1] + l1[i]
                l2.append(a)
            l1 = l2
            l2 = [1]
            n -= 1
        suma = 0
        for i in range(5):
            suma += (5 - i) * l1[i]
        return suma
