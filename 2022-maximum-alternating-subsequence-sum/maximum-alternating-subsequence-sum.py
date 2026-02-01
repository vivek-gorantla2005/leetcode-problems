from functools import lru_cache

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def dp(idx, even):
            if idx == len(nums):
                return 0
            
            notPick = dp(idx+1,even)

            total = nums[idx] if even else (-1 * nums[idx])

            pick = total + dp(idx+1,not even)

            return max(pick, notPick)
        
        return dp(0, True)