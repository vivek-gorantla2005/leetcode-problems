class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = set()
        
        def dfs(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])  
                return
            
            for x in nums:
                if x in used:
                    continue
                
                used.add(x)
                curr.append(x)
                
                dfs(curr)
                
                curr.pop()       # correct backtrack
                used.remove(x)
        
        dfs([])
        return ans