class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        peso5 = 0
        peso10 = 0
        for bill in bills:
            if bill == 5:
                peso5 += 1
            elif bill == 10:
                peso10 += 1
                if peso5:
                    peso5 -= 1
                else:
                    return False
            else:
                if peso10 and peso5:
                    peso5 -= 1
                    peso10 -= 1
                else:
                    if peso5 < 3:
                        return False
                    peso5 -= 3
        return True