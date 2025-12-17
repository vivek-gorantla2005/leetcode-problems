from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        n, m = len(heights), len(heights[0])
        pacific = [[False]*m for _ in range(n)]
        atlantic = [[False]*m for _ in range(n)]

        def dfs(i, j, visited, prevHeight):
            if (
                i < 0 or j < 0 or
                i >= n or j >= m or
                visited[i][j] or
                heights[i][j] < prevHeight
            ):
                return
            
            visited[i][j] = True

            dfs(i + 1, j, visited, heights[i][j])
            dfs(i - 1, j, visited, heights[i][j])
            dfs(i, j + 1, visited, heights[i][j])
            dfs(i, j - 1, visited, heights[i][j])

        # Pacific
        for j in range(m):
            dfs(0, j, pacific, heights[0][j])
        for i in range(n):
            dfs(i, 0, pacific, heights[i][0])

        # Atlantic
        for j in range(m):
            dfs(n - 1, j, atlantic, heights[n - 1][j])
        for i in range(n):
            dfs(i, m - 1, atlantic, heights[i][m - 1])

        # Cells reachable by both oceans
        result = []
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])

        return result
