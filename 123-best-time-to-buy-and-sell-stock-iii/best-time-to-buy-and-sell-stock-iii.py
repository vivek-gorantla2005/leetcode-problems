from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = {}

        def dfs(idx, buy, cap):
            if cap == 0:
                return 0
            if idx == n:
                return 0

            if (idx,buy,cap) in dp:
                return dp[(idx,buy,cap)]

            if buy:
                profit = max(
                    -prices[idx] + dfs(idx+1, 0, cap),   
                    dfs(idx+1, 1, cap)                  
                )
            else:
                profit = max(
                    prices[idx] + dfs(idx+1, 1, cap-1), 
                    dfs(idx+1, 0, cap)               
                )

            dp[(idx,buy,cap)] = profit
            return dp[(idx,buy,cap)]

        return dfs(0, 1, 2)