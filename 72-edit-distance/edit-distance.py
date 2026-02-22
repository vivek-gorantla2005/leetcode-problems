class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp = {}
        # def dfs(i,j):
        #     if i == 0:
        #         return j
        #     if j == 0:
        #         return i
        #     if (i,j) in dp:
        #         return dp[(i,j)]
        #     if word1[i-1] == word2[j-1]:
        #         return 0 + dfs(i-1,j-1)
            
        #     delete =  dfs(i-1,j)
        #     insert =  dfs(i,j-1)
        #     replace =   dfs(i-1,j-1) 
            
        #     dp[(i,j)] =  1 + min(delete,insert,replace)
        #     return dp[(i,j)]
        # n = len(word1)
        # m = len(word2)
        # return dfs(n,m)

        n = len(word1)
        m = len(word2)

        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j

        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    delete = dp[i-1][j]
                    insert = dp[i][j-1]
                    replace = dp[i-1][j-1]

                    dp[i][j] = 1 + min(delete, insert, replace)

        return dp[n][m]
                
