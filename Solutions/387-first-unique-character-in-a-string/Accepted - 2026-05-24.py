class Solution:
    def firstUniqChar(self, s: str) -> int:
        table = {}
        for i in range(len(s)):
            if s[i] not in table:
                table[s[i]] = i
            else:
                table[s[i]] = -1
        values = list(table.values())
        for i in range(len(values)):
            if values[i] != -1:
                return values[i]
        return -1