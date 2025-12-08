class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        nums.sort(reverse=True) 
        used = [False] * len(nums)

        def dfs(start, k, subsetSum):
            if k == 0:
                return True
            
            if subsetSum == target:
                return dfs(0, k - 1, 0)
            
            for i in range(start, len(nums)):
                if used[i] or subsetSum + nums[i] > target:
                    continue
                
                used[i] = True
                if dfs(i + 1, k, subsetSum + nums[i]):
                    return True
                used[i] = False
                
                if subsetSum == 0:
                    return False
            
            return False
        
        return dfs(0, k, 0)
