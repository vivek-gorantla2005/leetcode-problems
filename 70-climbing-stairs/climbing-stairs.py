from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def backtrack(steps):
            if steps == n:
                return 1
            if steps > n:
                return 0
            
            j1 = backtrack(steps+1)
            j2 = backtrack(steps+2)

            return j1+j2
        
        # dp = [0 for _ in range(n+1)]
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(2,n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        
        # return dp[n]

        prev1 = 1
        prev2 = 1
        curr = 0
        for i in range(2,n+1):
            curr = prev1+prev2
            prev2 = prev1
            prev1 = curr
        return prev1


