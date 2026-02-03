class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(idx):
            if idx >= len(nums):
                return 0
            
            if idx == len(nums)-1:
                return nums[idx]
            
            if idx in dp:
                return dp[idx]

            pick = nums[idx]+dfs(idx+2)
            notpick = 0 + dfs(idx+1)

            dp[idx] = max(pick,notpick)
            return dp[idx]
        
        return dfs(0)


        