class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        n = len(num)
        primes = [2, 3, 5, 7]
        factors = [0, 0, 0, 0]
        FACTORS = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0),
        }
        curr = t
        for i, N in enumerate(primes):
            while curr % N == 0:
                curr //= N
                factors[i] += 1
        if curr != 1:
            return "-1"
        
        def min_digits(need2, need3, need5, need7):
            digits = need5 + need7
            # 9 = 3 * 3
            digits += need3 // 2
            need3 %= 2
            # 8 = 2 * 2 * 2
            digits += need2 // 3
            need2 %= 3
            # 6 = 2 * 3
            if need2 >= 1 and need3 >= 1:
                digits += 1
                need2 -= 1
                need3 -= 1
            # 4 = 2 * 2
            if need2 == 2:
                digits += 1
            # 2 = 2
            elif need2 == 1:
                digits += 1
            # 3 = 3
            if need3:
                digits += 1
            return digits

        def build_minimum(length, need2, need3, need5, need7):
            result = []
            for pos in range(length):
                remaining = length - pos - 1
                for digit in range(1, 10):
                    f2, f3, f5, f7 = FACTORS[digit]
                    new2 = max(0, need2 - f2)
                    new3 = max(0, need3 - f3)
                    new5 = max(0, need5 - f5)
                    new7 = max(0, need7 - f7)
                    if min_digits(new2, new3, new5, new7) <= remaining:
                        result.append(str(digit))
                        need2 = new2
                        need3 = new3
                        need5 = new5
                        need7 = new7
                        break
            return "".join(result)
        
        length = min_digits(factors[0], factors[1], factors[2], factors[3])
        if length > n:
            return build_minimum(length, factors[0], factors[1], factors[2], factors[3])
        
        states = []
        need = tuple(factors)

        for i in range(n):
            digit = int(num[i])
            if digit == 0:
                break
            f2, f3, f5, f7 = FACTORS[digit]
            need = (max(0, need[0] - f2), max(0, need[1] - f3), max(0, need[2] - f5), max(0, need[3] - f7))
            states.append(need)
        if states[-1] == (0, 0, 0, 0) and "0" not in num:
            return num
        
        for i in range(n - 1, -1, -1):
            if i > len(states):
                continue
            if i == 0:
                need = tuple(factors)
            else:
                need = states[i - 1]
            int_digit = int(num[i])
            for digit in range(int_digit + 1, 10):
                f2, f3, f5, f7 = FACTORS[digit]
                new2 = max(0, need[0] - f2)
                new3 = max(0, need[1] - f3)
                new5 = max(0, need[2] - f5)
                new7 = max(0, need[3] - f7)
                remaining = n - i - 1
                if min_digits(new2, new3, new5, new7) <= remaining:
                    prefix = num[:i] + str(digit)
                    suffix = build_minimum(remaining, new2, new3, new5, new7)
                    return prefix + suffix

        return build_minimum(n + 1, factors[0], factors[1], factors[2], factors[3])

