class Solution:

    def minimumDistance(self, word: str) -> int:
        def getDistance(a, b):
            nonlocal alf
            return abs(alf[a][1] - alf[b][1]) + abs(alf[a][0] - alf[b][0])

        alf = dict()
        for i in range(26):
            alf[chr(ord("A") + i)] = (i//6, i % 6)
        n = len(word)
        ## dp[index][finger 1 position 0 - 25][finger 2 position 0 - 25]
        dp = [[[float("inf") for _ in range(26)] for _ in range(26)] for _ in range(n)]
        first = ord(word[0]) - ord('A')
        ## we can start at first char in every character 
        for j in range(26):
            dp[0][first][j] = 0
            dp[0][j][first] = 0

        # for each character 
        for i in range(1, n):
            curr = word[i]
            curr_index = ord(curr) - ord("A")

            ## get the distance from each char to the current one 
            ## all combinations of posible finger 1 and finger 2  
            for f1 in range(26):
                d1 = getDistance(curr, chr(ord("A") + f1))
                for f2 in range(26):
                    if dp[i-1][f1][f2] == float("inf"):
                        continue
                    ## move finger 1
                    dp[i][curr_index][f2] = min(dp[i][curr_index][f2], dp[i - 1][f1][f2] + d1)

                    ## move finger 2
                    d2 = getDistance(curr, chr(ord("A") + f2)) 
                    dp[i][f1][curr_index] = min(dp[i][f1][curr_index], dp[i - 1][f1][f2] + d2)
            
        out = float("inf")
        # get minumin to reach last char between al options
        for i in range(26):
            for j in range(26):
                out = min(out, dp[n - 1][i][j])

        return out