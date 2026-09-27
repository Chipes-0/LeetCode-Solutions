class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mapa = {}
        out = ""

        for key, value in knowledge:
            mapa[key] = value
        i = 0
        while i < len(s):
            if s[i] == "(":
                j = i + 1
                word = ""
                while s[j] != ")":
                    word += s[j]
                    j += 1
                if word in mapa:
                    out += mapa[word]
                else:
                    out += "?"
                i = j + 1
            else:
                out += s[i]
                i += 1
        return out