from typing import List

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def findParent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findParent(self.parent[node])  # path compression
        return self.parent[node]

    def unionBySize(self, u, v):
        pu = self.findParent(u)
        pv = self.findParent(v)

        if pu == pv:
            return False  # cycle detected

        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]

        return True
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n)

        for u, v in edges:
            if not dsu.unionBySize(u, v):
                return [u, v]
