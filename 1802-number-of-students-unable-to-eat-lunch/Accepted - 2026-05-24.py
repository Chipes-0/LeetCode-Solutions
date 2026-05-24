from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while sandwiches:
            student = students.pop(0)
            if student == sandwiches[0]:
                sandwiches.pop(0)
                count = 0
                continue
            students.append(student)
            count += 1
            if count == len(students):
                break
        return len(sandwiches)