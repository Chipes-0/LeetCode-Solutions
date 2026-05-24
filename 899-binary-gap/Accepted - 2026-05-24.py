class Solution:
    def binaryGap(self, n: int) -> int:
        arr = []
        n = bin(n)[2:]
        count = 0
        for i in range(len(n)):
            if n[i] == "1":
                if count:
                    arr.append(count)
                    count = 0
                arr.append("1")
            else:
                count += 1
        if arr[0] == 0:
            arr.pop(0)
        out = 0
        for i in range(1, len(arr) - 1):
            if arr[i] != "1" and arr[i - 1] == "1" and arr[i + 1] == "1":
                out = max(out, arr[i] + 1)
        return out