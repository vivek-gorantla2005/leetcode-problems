from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # build graph
        for a, b in prereq:
            adj[b].append(a)   # b → a
            indegree[a] += 1

        q = deque()

        # push nodes with indegree 0
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        count = 0

        ans = []

        while q:
            node = q.popleft()
            ans.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return len(ans) == numCourses