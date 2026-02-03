class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(idx):
            if idx >= len(nums):
                return 0
            
            if idx == len(nums)-1:
                return nums[idx]
            
            pick = nums[idx]+dfs(idx+2)
            notpick = 0 + dfs(idx+1)

            return max(pick,notpick)
        
        return dfs(0)


        