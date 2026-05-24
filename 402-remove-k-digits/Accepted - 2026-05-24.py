class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num = list(num)
        for i in range(len(num) - 1):
            if num[i] >= num[i - 1]:
                num[i] = ''
                k -= 1
            if k == 0: 
                break
        i = 0
        while num[i] not in "123456789" or num[i] == '':
            num[i] = ''
            i += 1
            if i == len(num):
                return "0"
        return ''.join(num) 