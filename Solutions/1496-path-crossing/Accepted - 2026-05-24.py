class Solution:
    def isPathCrossing(self, path: str) -> bool:
        coord = [0, 0]
        moves = {'N': (0, 1), 'S':(0, -1), 'E': (1, 0), 'W':(-1, 0)}
        for i in range(len(path)):
            coord[0] += moves[path[i]][0]
            coord[1] += moves[path[i]][1]
            if coord == [0, 0]:
                return True
        return False