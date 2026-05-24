class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat)
        k %= n
        copy = [row[:] for row in mat]
        while k:
            for i in range(n):
                if i & 1:
                    num = mat[i].pop(-1)
                    mat[i].insert(0, num)
                else:
                    num = mat[i].pop(0)
                    mat[i].append(num)
            k -= 1

        for i in range(n):
            for j in range(len(mat[i])):
                if copy[i][j] != mat[i][j]:
                    return False
        return True