class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp = {}

        # def dfs(idx, prevIdx):
        #     if idx == len(nums):
        #         return 0

        #     if (idx, prevIdx) in dp:
        #         return dp[(idx, prevIdx)]

        #     notPick = dfs(idx + 1, prevIdx)

        #     pick = 0
        #     if prevIdx == -1 or nums[idx] > nums[prevIdx]:
        #         pick = 1 + dfs(idx + 1, idx)

        #     dp[(idx, prevIdx)] = max(pick, notPick)
        #     return dp[(idx, prevIdx)]

        # return dfs(0, -1)

        # previdx starts from -1 but we cant store -1 in arr so perform idx+1 shift
        n = len(nums)
        # dp[i][prev+1]
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for prev in range(i - 1, -2, -1):
                notPick = dp[i + 1][prev + 1]

                pick = 0
                if prev == -1 or nums[i] > nums[prev]:
                    pick = 1 + dp[i + 1][i + 1]

                dp[i][prev + 1] = max(pick, notPick)

        return dp[0][0]


