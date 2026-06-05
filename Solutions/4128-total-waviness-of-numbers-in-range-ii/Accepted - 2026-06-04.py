class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def getPoints(num):
            if num < 100:
                return 0
            num = str(num)

            @cache 
            def dp(pos, prev2, prev1, length, tight):
                if pos == len(num):
                    return (0, 0, 1)
                ways, peaks, valleys = 0, 0, 0

                limit = int(num[pos]) if tight else 9 
                for i in range(limit + 1):
                    ntight = tight and (i == limit)

                    if length == 0:
                        if i == 0:
                            child = dp(pos + 1, 10, 10, length, ntight)
                        else:
                            child = dp(pos + 1, 10, i, length + 1, ntight)

                        peaks += child[0]
                        valleys += child[1]
                        ways += child[2]
                    
                    elif length == 1:
                        child = dp(pos + 1, prev1, i, 2, ntight)

                        peaks += child[0]
                        valleys += child[1]
                        ways += child[2]

                    else:
                        isPeak = 0
                        isValley = 0

                        if prev1 > prev2 and prev1 > i:
                            isPeak = 1

                        if prev1 < prev2 and prev1 < i:
                            isValley = 1

                        child = dp(pos + 1, prev1, i, 2, ntight)

                        ways += child[2]
                        peaks += child[0] + isPeak * child[2]
                        valleys += child[1] + isValley * child[2]

                return (peaks, valleys, ways)

            peaks, valleys, _ = dp(0, 10, 10, 0, True)
            return peaks + valleys

        a = getPoints(num1 - 1)
        b = getPoints(num2)
        return b - a