class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        current_row = [0] * 102
        previous_row = [poured] + [0] * 101

        row = 1
        while row <= query_row:
            for i in range(row):
                if previous_row[i] > 1:
                    current_row[i] += (previous_row[i] - 1) / 2
                    current_row[i + 1] += (previous_row[i] - 1) / 2
            previous_row = current_row
            current_row = [0] * 102
            row += 1
        if previous_row[query_glass] > 1:
            return 1 
        else: 
            return previous_row[query_glass]
