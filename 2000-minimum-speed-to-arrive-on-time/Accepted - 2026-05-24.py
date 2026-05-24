import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def timeAtSpeed(speed: int) -> int:
            ans = 0
            for d in dist[0:-1]:
                ans += math.ceil(d/speed)
            ans += dist[-1]/speed
            return ans

        if sum(dist) == hour:
            return 1
        if hour < len(dist) - 1:
            return -1
        
        left = 1
        right = max(dist)

        while left <= right:
            m = (left + right) // 2
            time = round(timeAtSpeed(m), 2)
            if time == hour:
                return m
            if time < hour:
                right = m - 1
            else:
                left = m +1
        return m 
        