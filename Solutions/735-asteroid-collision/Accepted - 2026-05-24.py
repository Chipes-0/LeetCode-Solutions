from typing import List
import numpy

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        def collisions(i: int, asteroids: List[int]) -> None:
            if i == len(asteroids):
                return 
            if numpy.sign(asteroids[i - 1]) != numpy.sign(asteroids[i]):
                asteroid1, asteroid2 = asteroids.pop(i - 1), asteroids.pop(i - 1)
                if abs(asteroid1) > abs(asteroid2):
                     asteroids.insert(i - 1, asteroid1)
                elif abs(asteroid1) < abs(asteroid2):
                    asteroids.insert(i - 1, asteroid2)
                collisions(i - 1, asteroids)
            else:
                collisions(i + 1, asteroids)
                

        collisions(1, asteroids)
        return asteroids