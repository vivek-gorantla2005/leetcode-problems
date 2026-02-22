class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        def dfs(i,j):
            if j < 0:
                return 1
            if i < 0:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]

            if s[i] == t[j]:
                dp[(i,j)] = dfs(i-1,j-1) + dfs(i-1,j)
                return dp[(i,j)]
            
            dp[(i,j)] = dfs(i-1,j)
            return dp[(i,j)]
        
        n = len(s)
        m = len(t)
        return dfs(n-1,m-1)
        