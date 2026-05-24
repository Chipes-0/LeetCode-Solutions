class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        i = 0
        while i + 1 != len(heights) and ((heights[i + 1] - heights[i]) or ladders > 0):
            print(i, bricks, ladders)
            if heights[i] >= heights[i + 1]:
                i += 1
            elif bricks >= (heights[i + 1] - heights[i]):
                bricks -= (heights[i + 1] - heights[i])
                i += 1
            elif ladders:
                ladders -= 1
                i += 1
            else:
                break
        return i