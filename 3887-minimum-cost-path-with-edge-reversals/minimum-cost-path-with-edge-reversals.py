class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u,2*w))

        dist = [float('inf')] * n
        dist[0] = 0

        pq = [(0, 0)]  # (cost, node)

        while pq:
            curr_dist, u = heapq.heappop(pq)

            if curr_dist > dist[u]:
                continue

            for v, wt in adj[u]:
                if dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
                    heapq.heappush(pq, (dist[v], v))

        return dist[n - 1] if dist[n - 1] != float('inf') else -1
