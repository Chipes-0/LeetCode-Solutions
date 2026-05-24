class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a = b = 0
        for i in range(len(colors) - 3):
            if colors[i: i + 3] == "AAA":
                a += 1
            elif colors[i: i + 3] == "BBB":
                b += 1
        return a > b
