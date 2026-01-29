class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = {}

        def dfs(i, j):
            if i == n - 1 and j == m - 1:
                return grid[i][j]

            if i < 0 or j < 0 or i >= n or j >= m:
                return float("inf")

            if (i, j) in dp:
                return dp[(i, j)]

            dp[(i, j)] = grid[i][j] + min(
                dfs(i, j + 1),
                dfs(i + 1, j)
            )
            return dp[(i, j)]

        return dfs(0, 0)
