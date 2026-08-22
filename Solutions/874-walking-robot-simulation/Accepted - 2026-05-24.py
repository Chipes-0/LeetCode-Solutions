class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        d = {}
        max_val = 0
        for obs in obstacles:
            d[(obs[0], obs[1])] = 1
        directions = [1, 1, -1, -1]
        movement = [0, 0]
        index = 0
        for element in commands:
            if element == -1:
                index = (index + 1) % 4
                continue
            elif element == -2:
                index = (index - 1) % 4
                continue
            else:
                for i in range(element):
                    if not (movement[1], movement[0]) in d:
                        movement[index % 2] += 1 * directions[index]
                    else:
                        movement[index % 2] -= 1 * directions[index]
                        break
                max_val = max(max_val, movement[0] ** 2 + movement[1] ** 2)
                    
        return max_val