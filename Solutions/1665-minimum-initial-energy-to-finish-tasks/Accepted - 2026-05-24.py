class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x : x[0] - x[1])

        total = tasks[0][1]
        curr = total - tasks[0][0]
        for actual, minimum in tasks[1:]:
            if curr < minimum:
                total += (minimum - curr)
                curr = minimum
            curr -= actual
        return total



        # """
        # # total = 3
        # energia actual = 3

        # 3 - 1 = 2
        # # total = 3
        # energia actual = 2

        # 2 + (4 - 2) = 2 + 2
        # 4 - 2 = 2
        # # total = 5
        # energia actual = 2

        # 2 + (12 - 2) = 2 + 10
        # 12 - 10 = 2
        # # total = 15
        # energia actual = 2

        # 2 + (11 - 2) = 2 + 9
        # 11 - 10 = 1
        # # total = 24
        # energia actual = 1

        # 1 + (9 - 1) = 1 + 8
        # 9 - 8 = 1
        # # total = 32
        # energia actual = 1
        # """