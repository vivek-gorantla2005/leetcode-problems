from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp = {}

        # def dfs(idx, buy, cap):
        #     if cap == 0:
        #         return 0
        #     if idx == n:
        #         return 0

        #     if (idx,buy,cap) in dp:
        #         return dp[(idx,buy,cap)]

        #     if buy:
        #         profit = max(
        #             -prices[idx] + dfs(idx+1, 0, cap),   
        #             dfs(idx+1, 1, cap)                  
        #         )
        #     else:
        #         profit = max(
        #             prices[idx] + dfs(idx+1, 1, cap-1), 
        #             dfs(idx+1, 0, cap)               
        #         )

        #     dp[(idx,buy,cap)] = profit
        #     return dp[(idx,buy,cap)]

        # return dfs(0, 1, 2)


        n = len(prices)

        nxt = [[0] * 3 for _ in range(2)]
        curr = [[0] * 3 for _ in range(2)]

        for idx in range(n-1,-1,-1):
            for buy in range(0,2):
                for cap in range(1,3):
                    if buy:
                        profit = max(
                            -prices[idx] + nxt[0][cap],   
                            nxt[1][cap]
                        )
                    else:
                        profit = max(
                            prices[idx] + nxt[1][cap-1], 
                            nxt[0][cap]               
                        )

                    curr[buy][cap] = profit
            nxt = curr

        return nxt[1][2]



