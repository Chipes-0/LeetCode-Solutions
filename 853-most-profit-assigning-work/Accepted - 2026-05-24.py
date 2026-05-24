class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        p_d = []
        out = 0
        for i in range(len(profit)):
            p_d.append((profit[i], difficulty[i]))
        p_d = sorted(p_d)[::-1]
        worker = sorted(worker)[::-1]
        job = 0
        for w in worker:
            while w < p_d[job][1]:
                job += 1
                if job >= len(p_d):
                    out += 0
                    break
            if job >= len(p_d):
                break
            out += p_d[job][0]
        return out