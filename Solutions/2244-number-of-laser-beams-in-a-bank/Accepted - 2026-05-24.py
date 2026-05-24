class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        index = 0
        for i in range(len(bank)):
            count = 0
            for d in bank[i]:
                if d == "1":
                    count += 1
            if count > 0:
                bank[index] = count
                index += 1
        bank = bank[:index]
        if len(bank) < 1:
            return 0
        out = 0
        while len(bank) > 1:
            out += bank.pop(0) * bank[0]
        return out