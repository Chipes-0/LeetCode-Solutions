class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [temperatures[0]]
        out = []
        for i in range(1, len(temperatures)):
            
            while stack[-1] <= temperatures[i]:
                stack.pop()
                
