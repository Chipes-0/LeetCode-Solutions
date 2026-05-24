class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        cinema = [[] for _ in range(n)]

        for rsv in reservedSeats:
            row, seat = rsv
            cinema[row - 1].append(seat)
        
        out = 0
        for row in cinema:
            line = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
            for element in row:
                line.remove(str(element))
            
            line = "".join(line)
            if "23456789" in line:
                out += 2
            elif "4567" in line:
                out += 1
            elif "2345" in line:
                out += 1
            elif "6789" in line:
                out += 1
        return out
