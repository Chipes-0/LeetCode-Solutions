class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = set([sublist[1] for sublist in trust])
        itrust = set([sublist[0] for sublist in trust])
        judge = trusted - itrust
        if judge:
            return judge.pop()
        return -1