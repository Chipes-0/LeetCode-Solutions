class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        out = []
        c = Counter(bulbs)
        for key, value in c.items():
            if value & 1:
                out.append(key)
            
        return out.sort()