from functools import lru_cache

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def dp(idx, sign):
            if idx == len(nums):
                return 0
            
            # Option 1: skip current element
            notPick = dp(idx + 1, sign)
            
            # Option 2: pick current element
            if sign == 0:   # +
                pick = nums[idx] + dp(idx + 1, 1)
            else:           # -
                pick = -nums[idx] + dp(idx + 1, 0)
            
            return max(pick, notPick)
        
        return dp(0, 0)