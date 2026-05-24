class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        curr_altitude = 0
        for g in gain:
            curr_altitude += g
            max_altitude = curr_altitude if curr_altitude > max_altitude else max_altitude
        return max_altitude
