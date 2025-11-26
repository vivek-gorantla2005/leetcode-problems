class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        n,m=len(grid),len(grid[0])
        dp = [[[-1] * k for _ in range(m)] for _ in range(n)]
        mod = 10**9+7
        def DFS(i,j,remain):
            if i == n-1 and j == m-1:
                remain = (remain + grid[i][j]) % k
                return 1 if remain == 0 else 0
            if i == n or j == m:
                return 0
            if dp[i][j][remain] > -1 :
                return dp[i][j][remain]
            dp[i][j][remain] = (
                DFS(i+1,j,((remain + grid[i][j]) % k))%mod+
                DFS(i,j+1,((remain + grid[i][j]) % k)) %mod
            )%mod
            return dp[i][j][remain]
        return DFS(0,0,0)