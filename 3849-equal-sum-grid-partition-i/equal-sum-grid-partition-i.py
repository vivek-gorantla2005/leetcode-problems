class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        
        prefix = [[0] * m for _ in range(n)]
        prefix[0][0] = grid[0][0]

        # 1st row
        for j in range(1, m):
            prefix[0][j] = prefix[0][j-1] + grid[0][j]

        # 1st column
        for i in range(1, n):
            prefix[i][0] = prefix[i-1][0] + grid[i][0]

        # fill prefix
        for i in range(1, n):
            for j in range(1, m):
                prefix[i][j] = (
                    prefix[i-1][j] 
                    + prefix[i][j-1] 
                    - prefix[i-1][j-1] 
                    + grid[i][j]
                )

        tot = prefix[n-1][m-1]

        # horizontal cuts
        for i in range(n):
            cutSum1 = prefix[i][m-1]
            cutSum2 = tot - cutSum1
            if cutSum1 == cutSum2:
                return True

        # vertical cuts
        for j in range(m):
            cutSum1 = prefix[n-1][j]
            cutSum2 = tot - cutSum1
            if cutSum1 == cutSum2:
                return True

        return False