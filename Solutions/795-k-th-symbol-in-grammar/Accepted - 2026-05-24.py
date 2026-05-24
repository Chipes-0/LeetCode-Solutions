class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        row = ['0']
        for i in range(n - 1):
            s = ""
            for digit in list(row[-1]):
                if digit == '0':
                    s += '01'
                else:
                    s += '10'
            row.append(s)
        return int(row[k - 1])