from functools import lru_cache

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)

        @lru_cache(None)
        def dfs(idx):
            if idx >= n:
                return 0

            # 1-day pass
            pass1 = costs[0] + dfs(idx + 1)

            # 7-day pass
            i = idx
            while i < n and days[i] < days[idx] + 7:
                i += 1
            pass2 = costs[1] + dfs(i)

            # 30-day pass
            i = idx
            while i < n and days[i] < days[idx] + 30:
                i += 1
            pass3 = costs[2] + dfs(i)

            return min(pass1, pass2, pass3)

        return dfs(0)
