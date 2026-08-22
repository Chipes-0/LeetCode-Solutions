class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        posMinutes = 6 * minutes
        hourMinute = minutes/60
        posHour = 30 * ((hour % 12) + hourMinute)
        return min(abs(posMinutes - posHour), 360 - abs(posMinutes - posHour))