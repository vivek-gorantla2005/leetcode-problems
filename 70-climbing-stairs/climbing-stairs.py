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
        
        return backtrack(0)