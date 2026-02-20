class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}
        # shift indexes by 1 place instead of zero indexed array take 1 based indexing
        def dfs(str1,str2,idx1,idx2):
            if idx1 == 0 or idx2 == 0:
                return 0
            
            if (idx1,idx2) in dp:
                return dp[(idx1,idx2)]

            if str1[idx1-1] == str2[idx2-1]:
                dp[(idx1,idx2)] = 1 + dfs(str1,str2,idx1-1,idx2-1)
                return dp[(idx1,idx2)]
            
            dp[(idx1,idx2)]  = max(dfs(str1,str2,idx1-1,idx2),dfs(str1,str2,idx1,idx2-1))
            return dp[(idx1,idx2)]

        rev = s[::-1]
        n = len(s)
        m = len(rev)

        return dfs(s,rev,n,m)