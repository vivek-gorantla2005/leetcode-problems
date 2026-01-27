class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        memo = {}
        
        def dfs(idx, time):
            if idx < 0:
                return 0
            
            if (idx, time) in memo:
                return memo[(idx, time)]

            pick = satisfaction[idx] * time + dfs(idx - 1, time + 1)
            notpick = dfs(idx - 1, time)
            
            memo[(idx, time)] = max(pick, notpick)
            return memo[(idx, time)]
        
        return dfs(len(satisfaction) - 1, 1)
