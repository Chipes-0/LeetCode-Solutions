from enum import Enum

class Values(Enum):
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
    for l in s:
        print(l)