class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mapeo = {}
        for i in range(len(names)):
            mapeo[heights[i]] = names[i]
        heights.sort()
        return [mapeo[x] for x in reversed(heights)]