class Solution:
    def longestPalindromeSubseq(self, text1: str) -> int:
        # dp = {}
        # # shift indexes by 1 place instead of zero indexed array take 1 based indexing
        # def dfs(str1,str2,idx1,idx2):
        #     if idx1 == 0 or idx2 == 0:
        #         return 0
            
        #     if (idx1,idx2) in dp:
        #         return dp[(idx1,idx2)]

        #     if str1[idx1-1] == str2[idx2-1]:
        #         dp[(idx1,idx2)] = 1 + dfs(str1,str2,idx1-1,idx2-1)
        #         return dp[(idx1,idx2)]
            
        #     dp[(idx1,idx2)]  = max(dfs(str1,str2,idx1-1,idx2),dfs(str1,str2,idx1,idx2-1))
        #     return dp[(idx1,idx2)]

        text2 = text1[::-1]
        n = len(text1)
        m = len(text2)

        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j]  = max(dp[i-1][j],dp[i][j-1])


        return dp[n][m]