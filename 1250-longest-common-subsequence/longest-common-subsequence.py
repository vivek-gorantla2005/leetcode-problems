class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        # shift indexes by 1 place instead of zero indexed array take 1 based indexing
        def dfs(idx1,idx2):
            if idx1 == 0 or idx2 == 0:
                return 0
            
            if (idx1,idx2) in dp:
                return dp[(idx1,idx2)]

            if text1[idx1-1] == text2[idx2-1]:
                dp[(idx1,idx2)] = 1 + dfs(idx1-1,idx2-1)
                return dp[(idx1,idx2)]
            
            dp[(idx1,idx2)]  = max(dfs(idx1-1,idx2),dfs(idx1,idx2-1))
            return dp[(idx1,idx2)]

        n = len(text1)
        m = len(text2)
        
        return dfs(n,m)
        