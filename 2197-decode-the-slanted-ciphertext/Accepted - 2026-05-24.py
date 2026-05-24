class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        out = ""
        m = len(encodedText) // rows
        mat = []
        for i in range(rows):
            mat.append(encodedText[i * m: (i + 1) * m])
        
        for start in range(m):
            i, j = 0, start
            while i < rows and j < m:
                out += mat[i][j]
                i += 1
                j += 1

        return out.strip()