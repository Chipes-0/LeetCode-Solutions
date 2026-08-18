class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ms = []
        out = 0
        for num in arr:
            if not ms:
                ms.append(num)
            else:
                while ms and num > ms[-1]:
                    ms.pop()
                if not ms:
                    out += 1
                ms.append(num)
        return out + 1