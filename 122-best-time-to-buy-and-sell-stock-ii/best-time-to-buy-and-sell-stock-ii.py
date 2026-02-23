class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        n = len(prices)
        def dp(idx,buy):
            if idx == n:
                return 0
            
            if (idx,buy) in memo:
                return memo[(idx,buy)]

            if buy:
                profit = max(
                    -prices[idx] + dp(idx+1,0),
                    0 + dp(idx+1,1)
                )
            else:
                profit = max(
                    prices[idx] + dp(idx+1,1),
                    0 + dp(idx+1,0)
                )
            
            memo[(idx,buy)] = profit
            return memo[(idx,buy)]

        return dp(0,1)