class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        restricted = set(restricted)
        visited.add(0)
        self.cnt = 0
        def dfs(node):
            visited.add(node)
            self.cnt+=1
            for i in adj[node]:
                if (i not in visited and i not in restricted):
                    dfs(i)

        dfs(0)
        return self.cnt

        