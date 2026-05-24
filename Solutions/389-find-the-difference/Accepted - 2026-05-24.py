class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        queue = []
        for i in range(len(s)):
            queue.append(s[i])
        for i in range(len(t)):
            if queue == []:
                return t[i]
            if queue[0] == t[i]:
                queue.pop(0)
            else:
                return t[i]