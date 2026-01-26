from collections import defaultdict, deque
from typing import List

class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        n, m = len(matrix), len(matrix[0])

        portals = defaultdict(list)
        for i in range(n):
            for j in range(m):
                if 'A' <= matrix[i][j] <= 'Z':
                    portals[matrix[i][j]].append((i, j))

        dq = deque()
        dq.append((0, 0, 0))  # dist, row, col

        visited = [[False]*m for _ in range(n)]
        used_portals = set()

        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        while dq:
            dist, r, c = dq.popleft()

            if visited[r][c]:
                continue
            visited[r][c] = True

            if r == n-1 and c == m-1:
                return dist

            # normal moves
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < m:
                    if not visited[nr][nc] and matrix[nr][nc] != '#':
                        dq.append((dist+1, nr, nc))

            # teleport (0 cost, once per letter)
            cell = matrix[r][c]
            if 'A' <= cell <= 'Z' and cell not in used_portals:
                used_portals.add(cell)
                for tr, tc in portals[cell]:
                    if not visited[tr][tc]:
                        dq.appendleft((dist, tr, tc))

        return -1
