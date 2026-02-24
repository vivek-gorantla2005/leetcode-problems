class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [[0] * n for _ in range(n)]
        # def dfs(idx, prevIdx):
        #     if idx == n:
        #         return 0

        #     if dp[idx][prevIdx + 1] != -1:
        #         return dp[idx][prevIdx + 1]

        #     notPick = dfs(idx + 1, prevIdx)

        #     pick = 0
        #     if prevIdx == -1 or nums[idx] > nums[prevIdx]:
        #         pick = 1 + dfs(idx + 1, idx)

        #     dp[idx][prevIdx + 1] = max(pick, notPick)
        #     return dp[idx][prevIdx + 1]

        # return dfs(0, -1)

# ====================================================> tabulation
        # n = len(nums)
        # dp = [[0] * (n+1) for _ in range(n+1)]

        # for idx in range(n-1, -1, -1):
        #     for prevIdx in range(idx-1, -2, -1):

        #         notPick = dp[idx + 1][prevIdx + 1]

        #         pick = 0
        #         if prevIdx == -1 or nums[idx] > nums[prevIdx]:
        #             pick = 1 + dp[idx + 1][idx + 1]

        #         dp[idx][prevIdx + 1] = max(pick, notPick)

        # return dp[0][0]
# ===========================================================================>space optimization

        n = len(nums)
        nxt = [0] * (n+1)
        curr = [0] * (n+1)

        for idx in range(n-1, -1, -1):
            for prevIdx in range(idx-1, -2, -1):
                notPick = nxt[prevIdx + 1]

                pick = 0
                if prevIdx == -1 or nums[idx] > nums[prevIdx]:
                    pick = 1 + nxt[idx + 1]

                curr[prevIdx + 1] = max(pick, notPick)
            
            nxt = curr

        return nxt[0]




        

        