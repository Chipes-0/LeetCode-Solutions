class Solution:
    def findLatestTime(self, s: str) -> str:
        word = []
        for i in range(len(s)):
            if s[i] == "?":
                if i == 0:
                    word.append("1")
                elif i == 1:
                    if word[-1] == "1":
                        word.append("1")
                    else:
                        word.append("0")
                elif i == 3:
                    word.append("5")
                elif i == 4:
                    word.append("9")
            else:
                word.append(s[i])
        return ''.join(word)