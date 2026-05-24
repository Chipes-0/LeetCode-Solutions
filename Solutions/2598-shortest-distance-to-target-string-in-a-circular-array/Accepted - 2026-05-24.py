class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        out = float("inf")
        n = len(words)
        n1, n2 = startIndex - 1, startIndex

        while words[n1] != target and words[n2] != target:
            if n1 == n2:
                return -1
            n1 = (n1 - 1) % n
            n2 = (n2 + 1) % n
        if words[n1] == target:
            out = min(out, abs(startIndex - n1))
        if words[n2] == target:
            out = min(out, abs(startIndex - n2))
        return out