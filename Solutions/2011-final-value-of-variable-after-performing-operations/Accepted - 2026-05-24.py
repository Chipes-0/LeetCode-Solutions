class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        out = 0
        for op in operations:
            if "+" in op:
                out += 1
            else: 
                out -= 1
        return out