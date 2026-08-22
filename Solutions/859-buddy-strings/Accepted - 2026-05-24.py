from collections import Counter

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return false
        if s == goal:
            frecuency = dict(Counter(s))
            for i in frecuency.values():
                if i >= 2:
                    return True
            return False
        indexes = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                indexes.append(i)
                if len(indexes) == 2:
                    break
        if len(indexes) % 2 == 1:
            return False
        sl = list(s)
        sl[indexes[0]], sl[indexes[1]] = sl[indexes[1]], sl[indexes[0]]
        return "".join(sl) == goal
        
        

