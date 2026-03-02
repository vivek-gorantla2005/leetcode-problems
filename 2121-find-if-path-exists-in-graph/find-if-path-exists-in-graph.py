from collections import defaultdict, deque
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        q = deque([source])
        vis = [False] * n
        vis[source] = True
        
        while q:
            node = q.popleft()
            
            if node == destination:
                return True
            
            for nei in adj[node]:
                if not vis[nei]:
                    vis[nei] = True
                    q.append(nei)
        
        return False