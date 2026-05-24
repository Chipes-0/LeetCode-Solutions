class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        indexes = list(range(n))
        stack = []
        out = []
        indexes.sort(key=lambda x: positions[x])
        for i in indexes:
            if directions[i] == 'R':
                stack.append(i)
            else:
                while stack and healths[i] > 0:
                    top_index = stack.pop()
                    if healths[top_index] > healths[i]:
                        healths[top_index] -= 1
                        healths[i] = 0
                        stack.append(top_index)
                    elif healths[top_index] < healths[i]:
                        healths[i] -= 1
                        healths[top_index] = 0
                    else:
                        healths[top_index] = 0
                        healths[i] = 0

        return [x for x in healths if x > 0]