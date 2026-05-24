class Solution:
    def maxLength(self, arr: List[str]) -> int:
        chars = set()
        def overlaping(set1, s):
            for i in range(len(s)):
                if s[i] in set1:
                    return True
            return False

        def backtrack(index):
            if index == len(arr):
                return len(chars)
            out = 0
            if not overlaping(chars, arr[index]):
                # take element at index
                for i in range(len(arr[index])):
                    chars.add(arr[index][i])
                # get next one
                out = backtrack(index + 1)
                # dont take element at index
                for i in range(len(arr[index])):
                    chars.remove(arr[index][i])
            return max(out, backtrack(index + 1))
        return backtrack(0)