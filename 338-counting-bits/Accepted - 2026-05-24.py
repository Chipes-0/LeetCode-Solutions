class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        for i in range(n + 1):
            print(out)
            if i in [0, 1]:
                out.append(i)
                continue
            out.append(out[i // 2] + (i % 2))
        return out