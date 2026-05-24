class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = sorted(happiness)[::-1]
        return int(sum(happiness[:k]) - (k * (k - 1) / 2))