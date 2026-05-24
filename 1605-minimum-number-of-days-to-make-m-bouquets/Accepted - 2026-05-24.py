class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            c = (left + right) // 2
            # print(m)
            consecutive = 0
            m_count = 0
            flag = False
            for day in bloomDay:
                if c >= day:
                    consecutive += 1
                else:
                    consecutive = 0
                if consecutive == k:
                    m_count += 1
                if m_count == m:
                    flag = True
                    break
            if flag:
                right = c - 1
            else:
                left = c + 1
        return left
            
