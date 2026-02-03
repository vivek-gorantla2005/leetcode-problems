class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2 :
            return max(nums)
        def helper(nums):
            prev1 = max(nums[0],nums[1])
            prev2 = nums[0]

            for i in range(2,len(nums)):
                pick = nums[i]+prev2
                notpick = prev1
                curr = max(pick,notpick)
                prev2 = prev1
                prev1 = curr
            
            return prev1
        
        return max(helper(nums[1:]),helper(nums[:-1]))

        