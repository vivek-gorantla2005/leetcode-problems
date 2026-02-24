class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        memo = {}

        def dp(idx, buy):
            if idx >= n:
                return 0

            if (idx, buy) in memo:
                return memo[(idx, buy)]

            if buy:
                profit = max(
                    -prices[idx] -fee + dp(idx + 1, 0),
                    dp(idx + 1, 1)
                )
            else:
                profit = max(
                    prices[idx] + dp(idx + 1, 1),
                    dp(idx + 1, 0)
                )

            memo[(idx, buy)] = profit
            return profit

        return dp(0, 1)
        