class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        def dfs(i,j):
            if i >= n or j >= m or i < 0 or j < 0 or (i,j) in visited or grid[i][j] == "0":
                return
            
            visited.add((i,j))
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and  (i,j) not in visited:
                    ans+=1
                    dfs(i,j)
        
        return ans