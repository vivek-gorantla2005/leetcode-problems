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

        # dp = [defaultdict(int) for _ in range(len(nums)+1)]
        # dp[0][0] = 1 #(0 elements,0 sum) -> 1 way

        # for i in range(len(nums)):
        #     for cur_sum,count in dp[i].items():
        #         dp[i+1][cur_sum + nums[i]] += count
        #         dp[i+1][cur_sum-nums[i]]+=count
        # return dp[len(nums)][target]
        
        dp = defaultdict(int) 
        dp[0] = 1 #(0 elements,0 sum) -> 1 way

        for i in range(len(nums)):
            nextdp = defaultdict(int)
            for cur_sum,count in dp.items():
                nextdp[cur_sum + nums[i]] += count
                nextdp[cur_sum-nums[i]]+=count
            dp = nextdp
        
        return dp[target]

