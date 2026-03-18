class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        #row
        n = len(grid)
        m = len(grid[0])
        s = 0
        ans = 0
        prefixMatrix = [[0] * m for _ in range(n)]
        prefixMatrix[0][0] = grid[0][0]
        #top row
        for i in range(1,m):
            prefixMatrix[0][i] = grid[0][i] + prefixMatrix[0][i-1]
            

        #top column
        for j in range(1,n):
            prefixMatrix[j][0]  = grid[j][0] + prefixMatrix[j-1][0]
        
        #fill remaining matrix
        for i in range(1, n):
            for j in range(1, m):
                prefixMatrix[i][j] = (
                    grid[i][j]
                    + prefixMatrix[i-1][j]
                    + prefixMatrix[i][j-1]
                    - prefixMatrix[i-1][j-1]
                )

        ans = 0
        for i in range(n):
            for j in range(m):
                if prefixMatrix[i][j] <= k :
                    ans+=1
        
        return ans


