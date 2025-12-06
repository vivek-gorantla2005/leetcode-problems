class Solution:
    def countPartitions(self, nums, k):
        from collections import deque
        
        n = len(nums)
        MOD = 10**9 + 7
        
        maxd = deque()
        mind = deque()
        
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        
        dp[0] = 1   # empty prefix = 1 way
        prefix[0] = 1
        
        l = 0
        
        for r in range(n):
            # maintain max deque
            while maxd and nums[maxd[-1]] < nums[r]:
                maxd.pop()
            maxd.append(r)

            # maintain min deque
            while mind and nums[mind[-1]] > nums[r]:
                mind.pop()
            mind.append(r)
            
            # shrink l while invalid
            while nums[maxd[0]] - nums[mind[0]] > k:
                l += 1
                if maxd[0] < l:
                    maxd.popleft()
                if mind[0] < l:
                    mind.popleft()
            
            # dp transition: sum(dp[l] ... dp[r])
            dp[r+1] = (prefix[r] - (prefix[l-1] if l > 0 else 0)) % MOD
            
            prefix[r+1] = (prefix[r] + dp[r+1]) % MOD
        
        return dp[n]
