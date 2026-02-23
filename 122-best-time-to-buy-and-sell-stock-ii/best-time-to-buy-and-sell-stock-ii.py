from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        dp = [[0] * 2 for _ in range(n+1)]

        for idx in range(n-1, -1, -1):
            for buy in range(2):
                if buy:
                    profit = max(
                        -prices[idx] + dp[idx+1][0],  # FIXED
                        dp[idx+1][1]
                    )
                else:
                    profit = max(
                        prices[idx] + dp[idx+1][1],   # FIXED
                        dp[idx+1][0]
                    )

                dp[idx][buy] = profit

        return dp[0][1]