class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp = {}
        # def dfs(idx):
        #     if idx >= len(nums):
        #         return 0
            
        #     if idx == len(nums)-1:
        #         return nums[idx]
            
        #     if idx in dp:
        #         return dp[idx]

        #     pick = nums[idx]+dfs(idx+2)
        #     notpick = 0 + dfs(idx+1)

        #     dp[idx] = max(pick,notpick)
        #     return dp[idx]
        
        # return dfs(0)

        if len(nums) <= 2 :
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            pick = nums[i]+dp[i-2]
            notpick = dp[i-1]
            dp[i] = max(pick,notpick)
        
        return dp[len(nums)-1]


        