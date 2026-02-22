class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def dfs(i,j):
            if i == 0:
                return j
            if j == 0:
                return i
            if (i,j) in dp:
                return dp[(i,j)]
            if word1[i-1] == word2[j-1]:
                return 0 + dfs(i-1,j-1)
            
            delete =  dfs(i-1,j)
            insert =  dfs(i,j-1)
            replace =   dfs(i-1,j-1) 
            
            dp[(i,j)] =  1 + min(delete,insert,replace)
            return dp[(i,j)]
        n = len(word1)
        m = len(word2)
        return dfs(n,m)
        