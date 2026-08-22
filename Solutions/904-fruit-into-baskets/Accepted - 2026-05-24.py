class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0 
        out = 0
        count = defaultdict(int)
        for right in range(len(fruits)):
            count[fruits[right]] += 1

            while len(count) > 2:
                count[fruits[left]] -= 1
                if not count[fruits[left]]:
                    del count[fruits[left]]
                left += 1
            out = max(right - left + 1, out)
        
            
        return out