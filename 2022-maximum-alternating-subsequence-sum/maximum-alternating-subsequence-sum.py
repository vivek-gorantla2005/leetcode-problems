class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i,flag):
            if i == len(nums):
                return 0
            
            if (i,flag) in dp:
                return dp[(i,flag)]

            notPick = dfs(i+1,flag)
            val = nums[i]
            if flag == False:
                val = -val
            pick = val + dfs(i+1,not flag)

            dp[(i,flag)] = max(pick,notPick)

            return dp[(i,flag)]
        
        return dfs(0,True)