class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        smallest = float("inf")
        odd_negatives = False
        total = 0
        for row in matrix:
            for element in row:
                smallest = min(smallest, abs(element))
                total += abs(element)
                if element < 0:
                    odd_negatives = not odd_negatives
        if odd_negatives:
            total -= smallest * 2
        
        return total