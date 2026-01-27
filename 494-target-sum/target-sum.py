from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def backtrack(idx,total):
            if idx == len(nums):
                return 1 if total == target else 0
            
            add = backtrack(idx+1,total+nums[idx])
            sub = backtrack(idx+1,total-nums[idx])
            return add+sub
        
        return backtrack(0,0)