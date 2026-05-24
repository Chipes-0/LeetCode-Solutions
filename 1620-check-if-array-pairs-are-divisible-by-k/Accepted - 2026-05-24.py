class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count = [0 for _ in range(k)]
        for num in arr:
            count[(num % k + k) % k] += 1
        
        if count[0] % 2 != 0:
            return False
        for i in range(1, k):
            if count[i] != count[k-i]:
                return False
        return True