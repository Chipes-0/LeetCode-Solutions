from typing import List

class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        out = None
        minDist = float("inf")
        for i, drone in enumerate(drones):
            dist = abs(drone[0] - target[0]) + abs(drone[1] - target[1])
            if dist <= drone[2] and dist < minDist:
                out = i
                minDist = dist
        if out != None:
            return out
        return -1