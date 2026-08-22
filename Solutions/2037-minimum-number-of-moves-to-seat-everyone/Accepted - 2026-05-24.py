class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        out = 0
        for i in range(len(students)):
            out += abs(students[i] - seats[i])
        return out