class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        exists = set()
        arr.sort()
        for val in arr:
            if val in exists:
                return True
            exists.add(val * 2)
        return False