class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def helper(nums,idx,curr):
            if idx == len(nums):
                self.ans.append(curr[:])
                return
            
            curr.append(nums[idx])
            helper(nums,idx+1,curr)
            curr.pop()
            helper(nums,idx+1,curr)
        curr = []
        helper(nums,0,curr)
        return self.ans


