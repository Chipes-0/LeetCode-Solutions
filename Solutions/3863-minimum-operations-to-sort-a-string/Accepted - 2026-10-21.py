class Solution:
    def minOperations(self, s: str) -> int:
        N = len(s)

        if N == 2:
            return 0 if s[0] <= s[1] else -1

        min_ch, min_i = s[0], 0
        max_ch, max_i = s[0], 0
        flag = True
        for i in range(N):
            if i >= 1 and flag:
                flag = s[i] >= s[i - 1]
            if s[i] < min_ch:
                min_ch = s[i]
                min_i = i
            if s[i] >= max_ch:
                max_ch = s[i]
                max_i = i
        
        ## Already sorted
        if flag:
            return 0
        ## All the same
        elif min_ch == max_ch:
            return 0
        ## Max at the beggining + min at the end
        elif min_i == N - 1 and max_i == 0:
            return 3
        ## Sort the middle
        elif min_i == 0 and max_i == N - 1:
            return 1
        ## Sort 1 side
        elif min_i == 0 or max_i == N - 1:
            return 1
        ## sort both sides
        else:
            return 2
        return -1
        