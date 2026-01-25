class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = set()
        def dfs(node):
            if node == destination:
                return True
            
            vis.add(node)

            for n in adj[node]:
                if n not in vis:
                    if dfs(n):
                        return True
            
            return False

        
        return dfs(source)
        
