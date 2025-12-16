from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, time = 0, 0
        rows, cols = len(grid), len(grid[0])
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        while q and fresh > 0:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (
                        nx < 0 or nx >= rows or
                        ny < 0 or ny >= cols or
                        grid[nx][ny] != 1
                    ):
                        continue

                    grid[nx][ny] = 2
                    q.append((nx, ny))
                    fresh -= 1

            time += 1

        return time if fresh == 0 else -1
