from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        ahead = [0] * 2

        for idx in range(n-1, -1, -1):
            curr = [0] * 2
            for buy in range(2):
                if buy:
                    profit = max(
                        -prices[idx] + ahead[0],  
                        ahead[1]
                    )
                else:
                    profit = max(
                        prices[idx] + ahead[1],
                        ahead[0]
                    )

                curr[buy] = profit
            
            ahead = curr

        return ahead[1]