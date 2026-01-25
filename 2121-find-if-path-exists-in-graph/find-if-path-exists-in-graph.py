class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = deque()
        q.append(source)
        vis = {(source)}
        while q:
            node = q.popleft()
            if node == destination:
                return True
            for curr in adj[node]:
                if curr not in vis:
                    q.append(curr)
                    vis.add(curr)
        
        return False
        
