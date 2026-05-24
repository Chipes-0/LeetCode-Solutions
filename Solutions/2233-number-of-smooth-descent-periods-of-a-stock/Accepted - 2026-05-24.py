class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        out = 0
        arr = []
        for p in prices:
            arr.append(p)
            if len(arr) > 1:
                if arr[-2] == arr[-1] + 1:
                    out += len(arr) -1
                else:
                    arr = [p]
            out += 1
        return out