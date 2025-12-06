class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()
        def helper(nums,idx,curr):
            if idx == len(nums):
                self.ans.append(curr[:])
                return
            
            curr.append(nums[idx])
            helper(nums,idx+1,curr)
            curr.pop()
            while idx+1 < len(nums) and nums[idx+1] == nums[idx]:
                idx+=1
            helper(nums,idx+1,curr)
        curr = []
        helper(nums,0,curr)
        return self.ans

