class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ps = [[0 for _ in range(3)] for _ in range(n + 1)]

        m = {"a" : 0, "b": 1, "c": 2}

        for i in range(1, n + 1):
            val = m[s[i - 1]]
            ps[i][0] = ps[i - 1][0]
            ps[i][1] = ps[i - 1][1]
            ps[i][2] = ps[i - 1][2]
            
            ps[i][val] += 1

        size = 0
        for i in range(n + 1):
            for j in range(i, n + 1):
                vals = [
                    ps[j][0] - ps[i][0],
                    ps[j][1] - ps[i][1],
                    ps[j][2] - ps[i][2]
                    ]
                flag = True
                same = None
                for v in vals:
                    if v != 0 and not same:
                        same = v
                    if v != 0 and v != same:
                        flag = False
                        break
                if flag and same:
                    size = max(size, j - i)
        return size