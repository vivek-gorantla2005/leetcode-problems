from functools import lru_cache

class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()

        position = []
        for pos, cap in factory:
            position.extend([pos] * cap)

        # def dfs(i, j):
        #     if i == len(robot):
        #         return 0
        #     if j == len(position):
        #         return float('inf')

        #     pick = abs(robot[i] - position[j]) + dfs(i + 1, j + 1)
        #     not_pick = dfs(i, j + 1)

        #     return min(pick, not_pick)

        n = len(robot)
        m = len(position)

        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(n):
            dp[i][m] = float('inf')

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                pick = abs(robot[i] - position[j]) + dp[i + 1][j + 1]
                not_pick = dp[i][j + 1]
                dp[i][j] = min(pick,not_pick)
        
        return dp[0][0]
