class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(idx,curr):
            if idx == len(nums):
                ans.append(curr[:])
                return 
            
            curr.append(nums[idx])
            dfs(idx+1,curr)
            curr.pop()
            dfs(idx+1,curr)

        dfs(0,[])
        return ans

        