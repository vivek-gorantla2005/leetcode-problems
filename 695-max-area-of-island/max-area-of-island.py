class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        self.ans = 0

        def dfs(i, j):
            if (
                i < 0 or j < 0 or
                i >= rows or j >= cols or
                visited[i][j] or
                grid[i][j] == 0
            ):
                return

            visited[i][j] = True
            self.ans+=1

            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)

        maxi = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    dfs(i, j)
                    maxi = max(maxi,self.ans)
                    self.ans = 0

        return maxi