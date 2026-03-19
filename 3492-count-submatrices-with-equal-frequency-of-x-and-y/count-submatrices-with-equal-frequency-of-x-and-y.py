class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        mat = [[[0, 0] for _ in range(m)] for _ in range(n)]
        ans = 0
        
        # (0,0)
        if grid[0][0] == 'X':
            mat[0][0] = [1, 0]
        elif grid[0][0] == 'Y':
            mat[0][0] = [0, 1]
        
        if mat[0][0][0] == mat[0][0][1] and mat[0][0][0] != 0:
            ans += 1
        
        # first row
        for j in range(1, m):
            mat[0][j] = mat[0][j-1][:]  
            
            if grid[0][j] == 'X':
                mat[0][j][0] += 1
            elif grid[0][j] == 'Y':
                mat[0][j][1] += 1
            
            if mat[0][j][0] == mat[0][j][1] and mat[0][j][0] != 0:
                ans += 1
        
        # first column
        for i in range(1, n):
            mat[i][0] = mat[i-1][0][:]
            
            if grid[i][0] == 'X':
                mat[i][0][0] += 1
            elif grid[i][0] == 'Y':
                mat[i][0][1] += 1
            
            if mat[i][0][0] == mat[i][0][1] and mat[i][0][0] != 0:
                ans += 1
        
        # rest of grid
        for i in range(1, n):
            for j in range(1, m):
                # inclusion-exclusion
                x = mat[i-1][j][0] + mat[i][j-1][0] - mat[i-1][j-1][0]
                y = mat[i-1][j][1] + mat[i][j-1][1] - mat[i-1][j-1][1]
                
                if grid[i][j] == 'X':
                    x += 1
                elif grid[i][j] == 'Y':
                    y += 1
                
                mat[i][j] = [x, y]
                
                if x == y and x != 0:
                    ans += 1
        
        return ans