class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apple.sort(reverse=True)
        capacity.sort(reverse=True)

        index = 0 
        total_c = 0
        total_apple = 0

        for a in apple:
            total_apple += a
            while total_c < total_apple:
                total_c += capacity[index]
                index += 1
        
        return index